instructions = []
for i in range(649):
    operation, value = input().split()
    value = int(value)
    instructions.append([operation, value])
accumulator = 0
visited = [False] * 649
counter = 0
while counter < 649:
    if visited[counter]:
        print(accumulator)
        break
    visited[counter] = True
    if instructions[counter][0] == 'acc':
        accumulator += instructions[counter][1]
        counter += 1
    elif instructions[counter][0] == 'jmp':
        counter += instructions[counter][1]
    else:
        counter += 1
