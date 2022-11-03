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
                        multiplier = 1
                        while x + multiplier * dx in range(ROW_COUNT) and y + multiplier * dy in range(COLUMN_COUNT):
                            if grid[x + multiplier * dx][y + multiplier * dy] == '#':
                                count += 1
                                break
                            elif grid[x + multiplier * dx][y + multiplier * dy] == 'L':
                                break
                            multiplier += 1
                if count == 0:
                    tmp[x][y] = '#'
                    changed = True
            elif grid[x][y] == '#':
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        multiplier = 1
                        while x + multiplier * dx in range(ROW_COUNT) and y + multiplier * dy in range(COLUMN_COUNT):
                            if grid[x + multiplier * dx][y + multiplier * dy] == '#':
                                count += 1
                                break
                            elif grid[x + multiplier * dx][y + multiplier * dy] == 'L':
                                break
                            multiplier += 1
                if count >= 5:
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
