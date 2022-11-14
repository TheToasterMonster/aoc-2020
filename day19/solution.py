import itertools

def process_rule(rule: str) -> list[str]:
    return list(map(str.strip, rule.split('|')))

FILE_PATH = "./input.txt"
rules: dict[int, list[str]] = {}
messages: list[str] = []
with open(FILE_PATH) as f:
    while line := f.readline().strip():
        number, rule = line.split(':')
        rules[int(number)] = process_rule(rule.replace('"', ''))
    while line := f.readline().strip():
        messages.append(line)

expanded_rules: dict[int, set[str]] = {}
def expand_rule(number: int) -> None:
    if number in expanded_rules:
        return
    need_to_expand = rules[number]
    if all(map(str.isalpha, need_to_expand)):
        expanded_rules[number] = rules[number]
        return

    expanded_rules[number] = set()
    for i, rule in enumerate(need_to_expand):
        numbers = list(map(int, rule.split()))
        patterns = ['']
        for n in numbers:
            expand_rule(n)
            patterns = set(map(lambda s: s[0] + s[1], itertools.product(patterns, expanded_rules[n])))
        expanded_rules[number] |= patterns

expand_rule(0)
count = 0
for message in messages:
    if message in expanded_rules[0]:
        count += 1
print(f'Part 1: {count}')

def match(s):
    # rule 0 means the string starts with rule 42 and ends with rule 31
    if len(s) % 8 != 0:
        return False
    
    count42 = 0
    while s and s[:8] in expanded_rules[42]:
        s = s[8:]
        count42 += 1
    
    count31 = 0
    while s and s[:8] in expanded_rules[31]:
        s = s[8:]
        count31 += 1
    
    return s == '' and 0 < count31 < count42

count = 0
for message in messages:
    if match(message):
        count += 1
print(f'Part 2: {count}')
