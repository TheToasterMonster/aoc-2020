module Solution where

import Control.Applicative
import Data.Char
import Data.Maybe

newtype Parser a = Parser { runParser :: String -> Maybe (a, String) }

type Operator = Char

data Atom = I Integer | O Operator
  deriving Show

data Expr = A Atom
          | Comb [Expr]
  deriving Show

satisfy :: (Char -> Bool) -> Parser Char
satisfy p = Parser f
  where
    f [] = Nothing
    f (x:xs)
      | p x = Just (x, xs)
      | otherwise = Nothing

char :: Char -> Parser Char
char c = satisfy (==c)

op :: Parser Operator
op = satisfy (\x -> x == '*' || x == '+')

posInt :: Parser Integer
posInt = Parser f
  where
    f xs
      | null ns   = Nothing
      | otherwise = Just (read ns, rest)
      where (ns, rest) = span isDigit xs

first :: (a -> b) -> (a, c) -> (b, c)
first f (x, y) = (f x, y)

instance Functor Parser where
  fmap f (Parser rf) = Parser $ fmap (first f) . rf

instance Applicative Parser where
  pure a = Parser $ \input -> Just (a, input)
  (Parser p1) <*> (Parser p2) = Parser $ \input -> do
    (f, input') <- p1 input 
    (a, input'') <- p2 input'
    Just (f a, input'')

instance Alternative Parser where
  empty = Parser (const Nothing)
  (Parser p1) <|> (Parser p2) = Parser $
    \input -> p1 input <|> p2 input

zeroOrMore :: Parser a -> Parser [a]
zeroOrMore p = Parser $
  \input -> case runParser p input of 
    Nothing -> Just (empty, input)
    Just (a, input') -> runParser ((:) <$> p <*> zeroOrMore p) input

oneOrMore :: Parser a -> Parser [a]
oneOrMore p = Parser $
  \input -> case runParser ((\x y -> [x, y]) <$> p <*> p) input of 
    Nothing -> runParser ((: []) <$> p) input
    Just (a, input') -> runParser ((:) <$> p <*> zeroOrMore p) input

spaces :: Parser String
spaces = zeroOrMore (satisfy isSpace)

parseAtom :: Parser Expr
parseAtom = A <$> ((O <$> op) <|> (I <$> posInt))

parseParen :: Parser Expr
parseParen = Comb <$>
  (spaces *> char '(' *> spaces *> elements <* char ')' <* spaces)
    where elements = oneOrMore (parseExpr <* spaces)

parseExpr :: Parser Expr
parseExpr = parseAtom <|> parseParen

reverseAll :: Expr -> Expr
reverseAll atom@(A _) = atom
reverseAll (Comb xs) = Comb $ reverse $ map reverseAll xs

getExpr :: String -> Expr
getExpr s = reverseAll $ fromMaybe (A $ I 0) $ fst <$> runParser parseExpr ("(" ++ s ++ ")")

eval :: Expr -> Integer
eval (A atom) = case atom of
  I num -> num
  _ -> undefined
eval (Comb []) = 0
eval (Comb [x]) = eval x
eval (Comb (x:op:xs)) = case op of
  A (O '*') -> eval x * eval (Comb xs)
  A (O '+') -> eval x + eval (Comb xs)
  _ -> undefined

flatten :: Expr -> Expr
flatten (Comb [x]) = flatten x
flatten (Comb xs) = Comb (map flatten xs)
flatten x = x

process :: Expr -> Expr
process atom@(A _) = atom
process (Comb (x:op:y:xs)) = case op of
  A (O '+') -> process $ Comb ((Comb [process x, op, process y]) : xs)
  _ -> Comb (process x : rest)
    where Comb rest = process (Comb (op:y:xs))
process (Comb [x, y]) = Comb [process x, process y]
process x = x

filePath :: FilePath
filePath = "./input.txt"

solve1 :: String -> Integer
solve1 = sum . map (eval . getExpr) . lines

solve2 :: String -> Integer
solve2 = sum . map (eval . process . flatten . getExpr) . lines

toString :: Expr -> String
toString (A (I i)) = show i
toString (A (O o)) = [o]
toString (Comb xs) = "(" ++ concatMap toString xs ++ ")"

main :: IO ()
main = do
  fileStr <- readFile filePath
  putStr "Part 1: "
  print $ solve1 fileStr
  putStr "Part 2: "
  print $ solve2 fileStr
