FILE_SIZE = 542
instructions = []
for _ in range(FILE_SIZE):
    command, val = input().split(" = ")
    if command != "mask":
        command = int(command[command.find('[') + 1:command.find(']')])
        val = int(val)
    instructions.append([command, val])

mem = {}
def initialize(loc, val, mask=''):
    if mask:
        loc = list(bin(loc)[2:].rjust(36, '0'))
        for i in range(36):
            if mask[i] == 'X':
                loc[i] = 'X'
            elif mask[i] == '1':
                loc[i] = '1'
        initialize(loc.copy(), val)
    else:
        if 'X' in loc:
            ind = loc.index('X')
            loc[ind] = '0'
            initialize(loc.copy(), val)
            loc[ind] = '1'
            initialize(loc.copy(), val)
        else:
            loc = int("0b" + "".join(loc), base=2)
            mem[loc] = val


mask = ""
for command, val in instructions:
    if command == "mask":
        mask = val
    else:
        initialize(command, val, mask)
print(sum(mem.values()))
