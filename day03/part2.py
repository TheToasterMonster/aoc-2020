biome_map = []
for i in range(323):
    biome_map.append(input())
width = len(biome_map[0])
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = []
for dx, dy in slopes:
    x, y = 0, 0
    count = 0
    while x < 323:
        if biome_map[x][y] == '#':
            count += 1
        x += dx
        y = (y + dy) % width
    trees.append(count)
prod = 1
for i in trees:
    prod *= i
print(prod)
