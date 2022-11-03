FILE_PATH = "input.txt"

valid = set()
yours = None
nearby = []
fields = []
valid_ranges = []

with open(FILE_PATH) as f:
    while l := f.readline().strip():
        line = l[l.index(':'):]
        field = l[:l.index(':')]
        fields.append(field)

        tokens = list(filter(None, line.split()))
        ranges = tokens[1::2]
        ranges = list(map(lambda x : tuple(int(i) for i in x.split('-')), ranges))

        local_valid = set()
        for low, high in ranges:
            for i in range(low, high + 1):
                local_valid.add(i)
        valid_ranges.append(local_valid)
        valid |= local_valid

    f.readline()
    yours = list(map(int, filter(None, f.readline().strip().split(','))))

    f.readline()
    f.readline()
    while line := f.readline().strip():
        ticket = list(map(int, filter(None, line.split(','))))
        nearby.append(ticket)

valid_tickets = []
error = 0
for ticket in nearby:
    invalid = False
    for i in ticket:
        if i not in valid:
            error += i
            invalid = True
    if not invalid:
        valid_tickets.append(ticket)
print(f'Part 1: {error}')

can_be = {i: set(range(len(fields))) for i in range(len(fields))}
for ticket in valid_tickets:
    for i, value in enumerate(ticket):
        for j in can_be:
            if i in can_be[j] and value not in valid_ranges[j]:
                can_be[j].remove(i)

order = list((key, can_be[key]) for key in can_be)
order.sort(key=lambda pr: len(pr[1]))
used = set()
assoc = {}
for field, possible in order:
    possible -= used
    assoc[field] = list(possible)[0]
    used |= possible

field_assoc = list((key, assoc[key]) for key in assoc)
field_assoc.sort()
prod = 1
for field, ind in field_assoc:
    if fields[field].startswith('departure'):
        prod *= yours[ind]
print(f'Part 2: {prod}')
