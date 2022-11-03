biome_map = []
for i in range(323):
    biome_map.append(input())
width = len(biome_map[0])
x, y = 0, 0
trees = 0
while x < 323:
    if biome_map[x][y] == '#':
        trees += 1
    x += 1
    y = (y + 3) % width
print(trees)
