from input import get

print('starting...')

text = get(4)
lines = text.splitlines()

print('parsing...')

# expected fields:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) <-- optional

# input ex:
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valids = 0
passports = [{}]
idx = 0

for i in range(len(lines)):
    # empty lines denote new passports
    if len(lines[i]) < 1:
        idx += 1
        continue

    if idx >= len(passports):
        passports.append({})

    entry = passports[idx]
    line = lines[i].split(' ')

    for l in line:
        field = l.split(':')
        # TODO: Check if field already exists
        entry[field[0]] = field[1]

    passports[idx] = entry

print('working...')

def validator(pp):
    # rules:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    if len(pp['byr']) != 4 or len(pp['iyr']) != 4 or len(pp['eyr']) != 4 or len(pp['pid']) != 9 or len(pp['hcl']) != 7:
        return False
    if int(pp['byr']) < 1920 or int(pp['byr']) > 2002 or int(pp['iyr']) < 2010 or int(pp['iyr']) > 2020 or int(pp['eyr']) < 2020 or int(pp['eyr']) > 2030:
        return False
    if not pp['pid'].isnumeric():
        return False
    if 'cm' not in pp['hgt'] and 'in' not in pp['hgt']:
        return False;

    if 'cm' in pp['hgt']:
        hgt = int(pp['hgt'].strip('cm'))

        if hgt < 150 or hgt > 193:
            return False

    if 'in' in pp['hgt']:
        hgt = int(pp['hgt'].strip('in'))

        if hgt < 59 or hgt > 76:
            return False

    if pp['ecl'] not in ['amb', 'brn', 'blu', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if pp['hcl'][0] != '#':
        return False

    try:
        int(pp['hcl'][1:], 16)
        return True
    except ValueError:
        return False

for p in passports:
    valid = True

    for field in fields:
        if field not in p:
            valid = False
            break

    if not valid:
        continue

    valid = validator(p)

    if valid:
        valids += 1

print('valids: ' + str(valids))

print('done')
