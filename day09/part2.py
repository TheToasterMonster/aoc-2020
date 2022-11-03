FILE_SIZE = 1000
PREAMBLE_LENGTH = 25
nums = []
for i in range(FILE_SIZE):
    nums.append(int(input()))

for i in range(PREAMBLE_LENGTH, FILE_SIZE):
    prev = nums[i - PREAMBLE_LENGTH:i]
    counterparts = set()
    found = False
    for j in prev:
        if nums[i] - j in counterparts:
            found = True
            break
        else:
            counterparts.add(j)
    if not found:
        target = nums[i]
        break

sums = {}
for i in range(FILE_SIZE):
    sums[i] = {}
    sums[i][nums[i]] = i
    if i - 1 >= 0:
        for j in sums[i - 1]:
            sums[i][j + nums[i]] = sums[i - 1][j]
for i in range(FILE_SIZE):
    if target in sums[i] and i != sums[i][target]:
        print(min(nums[sums[i][target]:i + 1]) + max(nums[sums[i][target]:i + 1]))
        break
