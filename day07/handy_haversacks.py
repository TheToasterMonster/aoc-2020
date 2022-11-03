bag_parents = {}
for i in range(594):
    parent, children = input().split(' contain ')
    children = list(map(lambda x: x[2:], children.split(', ')))
    for child in children:
        if child[-1] == '.':
            child = child[:-1]
        if child[-1] != 's':
            child += 's'
        if child in bag_parents:
            bag_parents[child].append(parent)
        else:
            bag_parents[child] = [parent]

count = 0
already_seen = set()
def search(bag):
    if bag not in bag_parents:
        return
    global count
    for parent in bag_parents[bag]:
        if parent in already_seen:
            continue;
        else:
            count += 1
            already_seen.add(parent)
            search(parent)

search('shiny gold bags')
print(count)
