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

mx = 0
for i in range(867):
    code = input()
    mx = max(mx, id(code))
print(mx)
