passports = []
passport = ""
for i in range(999):
    field = input()
    if field == "":
        passports.append(passport)
        passport = ""
    else:
        passport += field
passports.append(passport)
required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
count = 0
for passport in passports:
    valid = True
    for field in required:
        if field not in passport:
            valid = False
            break
    if valid:
        count += 1
print(count)
