nums = []
for i in range(1000):
    nums.append(int(input()))

for i in range(25, 1000):
    prev_25 = nums[i - 25:i]
    counterparts = set()
    found = False
    for j in prev_25:
        if nums[i] - j in counterparts:
            found = True
            break
        else:
            counterparts.add(j)
    if not found:
        print(nums[i])
        break
