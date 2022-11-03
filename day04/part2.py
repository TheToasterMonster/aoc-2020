def check_byr(val):
    return int(val) in range(1920, 2003)

def check_iyr(val):
    return int(val) in range(2010, 2021)

def check_eyr(val):
    return int(val) in range(2020, 2031)

def check_hgt(val):
    if "cm" in val:
        return int(val[:len(val) - 2]) in range(150, 194)
    elif "in" in val:
        return int(val[:len(val) - 2]) in range(59, 77)
    else:
        return False

def check_hcl(val):
    if val[0] == '#':
        code = val[1:]
        if len(code) == 6:
            for i in code:
                if i not in '0123456789abcdef':
                    return False
            return True
        else:
            return False
    else:
        return False

def check_ecl(val):
    allowed = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return val in allowed

def check_pid(val):
    if len(val) != 9:
        return False
    for i in val:
        if i not in '0123456789':
            return False
    return True

passports = []
passport = ""
for i in range(999):
    field = input()
    if field == "":
        passports.append(passport)
        passport = ""
    else:
        passport += ' ' + field
passports.append(passport)
required = {"byr": check_byr, "iyr": check_iyr, "eyr": check_eyr, "hgt": check_hgt, "hcl": check_hcl, "ecl": check_ecl, "pid": check_pid}
count = 0
for passport in passports:
    fields = {}
    for key, val in [i.split(':') for i in passport.split()]:
        fields[key] = val
    valid = True
    for field in required:
        if field not in fields or not required[field](fields[field]):
            valid = False
            break
    if valid:
        count += 1
print(count)
