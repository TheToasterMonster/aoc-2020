arr = []
for i in range(200):
    arr.append(int(input()))
nums = set()
for i in arr:
    if 2020 - i in nums:
        print(i * (2020 - i))
        break
    else:
        nums.add(i)
