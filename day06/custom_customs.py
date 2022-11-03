groups = []
group_response = ""
for i in range(2257):
    answer = input()
    if answer == "":
        groups.append(group_response)
        group_response = ""
    else:
        group_response += answer
groups.append(group_response)
groups_count = []
for group in groups:
    groups_count.append(len(set(group)))
print(sum(groups_count))
