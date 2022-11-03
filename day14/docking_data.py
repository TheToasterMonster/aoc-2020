instructions = []
for _ in range(542):
    command, val = input().split(" = ")
    if command != "mask":
        command = int(command[command.find('[') + 1:command.find(']')])
        val = int(val)
    instructions.append([command, val])

mem = {}
def initialize(loc, val, mask):
    val = list(bin(val)[2:].rjust(36, '0'))
    for i in range(36):
        if mask[i] == 'X':
            continue
        else:
            val[i] = mask[i]

    mem[loc] = int("0b" + "".join(val), base=2)

mask = ""
for command, val in instructions:
    if command == "mask":
        mask = val
    else:
        initialize(command, val, mask)
print(sum(mem.values()))
