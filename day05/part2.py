def id(code):
    L, R = 0, 127
    for i in code[:7]:
        mid = L + (R - L) // 2
        if i == 'F':
            R = mid
        else:
            L = mid + 1
    row = L
    L, R = 0, 7
    for i in code[7:]:
        mid = L + (R - L) // 2
        if i == 'L':
            R = mid
        else:
            L = mid + 1
    col = L
    return 8 * row + col

seats = []
for i in range(867):
    code = input()
    seats.append(id(code))
mx, mn = max(seats), min(seats)
total_sum = mx * (mx + 1) // 2 - mn * (mn - 1) // 2
actual_sum = sum(seats)
missing = total_sum - actual_sum
print(missing)
