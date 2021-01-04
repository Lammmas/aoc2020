from input import get

print('starting...')

text = get(2)
lines = text.splitlines()
valid = 0

print('parsing...')

for line in lines:
    values = str(line).split(' ') # ex: ['11-15','d:','ddddddddddzdpdn']
    limits = values[0].split('-')
    min = int(limits[0])
    max = int(limits[1])
    needed = values[1].strip(':')

    match = 0

    if values[2][min - 1] == needed:
        match += 1

    if values[2][max - 1] == needed:
        match += 1

    if match == 1:
        valid += 1

print('valid: ' + str(valid))

print('done')
