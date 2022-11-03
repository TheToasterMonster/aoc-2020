bag_contains = {}
for i in range(594):
    parent, children = input().split(' contain ')
    if children == 'no other bags.':
        continue
    bag_contains[parent] = {}
    children = children.split(', ')
    for child in children:
        if child[-1] == '.':
            child = child[:-1]
        if child[-1] != 's':
            child += 's'
        num, color = int(child[0]), child[2:]
        bag_contains[parent][color] = num

count = 0
def search(bag, quantity):
    if bag not in bag_contains:
        return
    global count
    count += (quantity * sum(bag_contains[bag].values()))
    for child in bag_contains[bag]:
        search(child, quantity * bag_contains[bag][child])

search('shiny gold bags', 1)
print(count)
