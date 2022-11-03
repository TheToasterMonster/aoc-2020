arr = []
for i in range(200):
    arr.append(int(input()))
found = False
for i in arr:
    target = 2020 - i
    tmp = arr.copy()
    tmp.remove(i)
    nums = set()
    for j in tmp:
        if target - j in nums:
            print(i * j * (target - j))
            found = True
            break
        else:
            nums.add(j)
    if found:
        break
