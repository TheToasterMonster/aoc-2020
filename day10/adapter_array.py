FILE_SIZE = 92
arr = []
for i in range(FILE_SIZE):
    arr.append(int(input()))
arr.append(0)
arr.sort()
arr.append(arr[-1] + 3)

one_diff = 0
three_diff = 0
for i in range(1, FILE_SIZE + 2):
    if arr[i] - arr[i - 1] == 1:
        one_diff += 1
    elif arr[i] - arr[i - 1] == 3:
        three_diff += 1
print(one_diff * three_diff)
