from copy import deepcopy

FILE_SIZE = 649
instructions = []
for i in range(FILE_SIZE):
    operation, value = input().split()
    value = int(value)
    instructions.append([operation, value])

def check_loop(instructions):
    visited = [False] * FILE_SIZE
    counter = 0
    while counter < FILE_SIZE:
        if visited[counter]:
            return True
        visited[counter] = True
        if instructions[counter][0] == 'acc':
            counter += 1
        elif instructions[counter][0] == 'jmp':
            counter += instructions[counter][1]
        else:
            counter += 1
    return False

found_result = False
if not found_result:
    jmp = [i for i in range(FILE_SIZE) if instructions[i][0] == 'jmp']
    for command in jmp:
        tmp = deepcopy(instructions)
        tmp[command][0] = 'nop'
        if not check_loop(tmp):
            found_result = True
            instructions = tmp
            break
if not found_result:
    nop = [i for i in range(FILE_SIZE) if instructions[i][0] == 'nop']
    for command in nop:
        tmp = deepcopy(instructions)
        tmp[command][0] = 'jmp'
        if not check_loop(tmp):
            found_result = True
            instructions = tmp
            break

accumulator = 0
counter = 0
while counter < FILE_SIZE:
    if instructions[counter][0] == 'acc':
        accumulator += instructions[counter][1]
        counter += 1
    elif instructions[counter][0] == 'jmp':
        counter += instructions[counter][1]
    else:
        counter += 1
print(accumulator)
