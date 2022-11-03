FILE_SIZE = 762
instructions = []
for i in range(FILE_SIZE):
    instr = input()
    instructions.append([instr[0], int(instr[1:])])

location = [0, 0]
directions = ['E', 'N', 'W', 'S']
facing = 0
def move(instruction, value):
    global facing
    if instruction == 'N':
        location[1] += value
    elif instruction == 'S':
        location[1] -= value
    elif instruction == 'E':
        location[0] += value
    elif instruction == 'W':
        location[0] -= value
    elif instruction == 'L':
        facing = ((facing + value // 90) % 4 + 4) % 4
    elif instruction == 'R':
        facing = ((facing - value // 90) % 4 + 4) % 4
    else:
        move(directions[facing], value)

for i in instructions:
    move(i[0], i[1])
print(abs(location[0]) + abs(location[1]))
