FILE_SIZE = 92
arr = []
for i in range(FILE_SIZE):
    arr.append(int(input()))
arr.append(0)
arr.sort()
arr.append(arr[-1] + 3)

sums = [0] * (FILE_SIZE + 2)
sums[0] = 1
for i in range(1, FILE_SIZE + 2):
    for j in range(1, 4):
        if i - j >= 0 and arr[i] - arr[i - j] <= 3:
            sums[i] += sums[i - j]
print(sums[-1])
