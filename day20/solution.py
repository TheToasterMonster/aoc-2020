import itertools

INPUT_FILE = "./input.txt"
images: dict[int, list[str]] = {}
with open(INPUT_FILE) as f:
    while header := f.readline().strip():
        idNum = int(header.split()[1][:-1])
        lines: list[str] = []
        while line := f.readline().strip():
            lines.append(line)
        images[idNum] = lines

def getSides(image: list[str]):
    top = image[0]
    bot = image[-1]
    left = "".join(row[0] for row in image)
    right = "".join(row[-1] for row in image)
    sides = [top, bot, left, right]
    return sides + list(map(lambda s: "".join(reversed(s)), sides))

print("\n".join(images[3529]))
print(getSides(images[3529]))

rowCounts: dict[str, list[int]] = {}
for imageID in images:
    for side in getSides(images[imageID]):
        if side not in rowCounts:
            rowCounts[side] = []
        rowCounts[side].append(imageID)

singles: dict[int, int] = {}
for row in rowCounts:
    side = rowCounts[row]
    if len(side) == 1:
        if side[0] not in singles:
            singles[side[0]] = 0
        singles[side[0]] += 1


corners: set[int] = set()
for single in singles:
    if singles[single] == 4:
        corners.add(single)

prod = 1
for i in corners:
    prod *= i
print(f'Part 1: {prod}')
