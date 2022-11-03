FILE_SIZE = 762
instructions = []
for i in range(FILE_SIZE):
    instr = input()
    instructions.append([instr[0], int(instr[1:])])

location = [0, 0]
waypoint = [10, 1]
directions = ['E', 'N', 'W', 'S']
def rotate90(point, center):
    point[0] -= center[0]
    point[1] -= center[1]
    point[0], point[1] = -point[1], point[0]
    point[0] += center[0]
    point[1] += center[1]

def move(instruction, value):
    if instruction == 'N':
        waypoint[1] += value
    elif instruction == 'S':
        waypoint[1] -= value
    elif instruction == 'E':
        waypoint[0] += value
    elif instruction == 'W':
        waypoint[0] -= value
    elif instruction == 'L':
        for i in range((value // 90 + 4) % 4):
            rotate90(waypoint, location)
    elif instruction == 'R':
        for i in range(((-value // 90) % 4 + 4) % 4):
            rotate90(waypoint, location)
    else:
        for i in range(value):
            dx, dy = waypoint[0] - location[0], waypoint[1] - location[1]
            waypoint[0] += dx
            waypoint[1] += dy
            location[0] += dx
            location[1] += dy

for i in instructions:
    move(i[0], i[1])
print(abs(location[0]) + abs(location[1]))
