groups = []
group_response = ""
for i in range(2257):
    answer = input()
    if answer == "":
        groups.append(group_response)
        group_response = ""
    else:
        group_response += ' ' + answer
groups.append(group_response)
groups_count = []
for group in groups:
    responses = group.split()
    common = set(responses[0])
    for i in range(1, len(responses)):
        to_remove = set()
        for response in common:
            if response not in responses[i]:
                to_remove.add(response)
        for response in to_remove:
            common.remove(response)
    groups_count.append(len(common))
print(sum(groups_count))
