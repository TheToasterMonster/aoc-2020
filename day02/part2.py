valid_passwords = 0
for i in range(1000):
    policy, letter, password = input().split()
    first, second = map(int, policy.split('-'))
    letter = letter[0]
    if password[first - 1] == letter or password[second - 1] == letter:
        if password[first - 1] == letter and password[second - 1] == letter:
            continue
        else:
            valid_passwords += 1
print(valid_passwords)
