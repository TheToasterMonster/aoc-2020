from copy import deepcopy
ROW_COUNT = 97
grid = []
for i in range(ROW_COUNT):
    grid.append(list(input()))

COLUMN_COUNT = len(grid[0])
def move():
    global grid
    changed = False
    tmp = deepcopy(grid)
    for x in range(ROW_COUNT):
        for y in range(COLUMN_COUNT):
            if grid[x][y] == 'L':
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if x + dx < 0 or x + dx >= ROW_COUNT:
                            continue
                        if y + dy < 0 or y + dy >= COLUMN_COUNT:
                            continue
                        if grid[x + dx][y + dy] == '#':
                            count += 1
                if count == 0:
                    tmp[x][y] = '#'
                    changed = True
            elif grid[x][y] == '#':
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if x + dx < 0 or x + dx >= ROW_COUNT:
                            continue
                        if y + dy < 0 or y + dy >= COLUMN_COUNT:
                            continue
                        if grid[x + dx][y + dy] == '#':
                            count += 1
                if count >= 4:
                    tmp[x][y] = 'L'
                    changed = True
    grid = tmp
    return changed
                
while move():
    continue

count = 0
for i in range(ROW_COUNT):
    for j in range(COLUMN_COUNT):
        if grid[i][j] == '#':
            count += 1
print(count)
