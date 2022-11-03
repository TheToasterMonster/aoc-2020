valid_passwords = 0
for i in range(1000):
    policy, letter, password = input().split()
    min, max = map(int, policy.split('-'))
    letter = letter[0]
    count = 0
    for i in password:
        if i == letter:
            count += 1
    if min <= count and count <= max:
        valid_passwords += 1
print(valid_passwords)
