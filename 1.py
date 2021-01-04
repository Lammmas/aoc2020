lines = []

print('starting...')

with open('1.txt', 'r') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = int(lines[i])

print('parsed')

for val in lines:
    diff = 2020 - val

    if diff in lines:
        res = val * diff
        print("%s * %s = %s" % (val, diff, res))
        break

print('part 1 done')

res = 0

for first in lines:
    spare = 2020 - first

    for second in lines:
        diff = spare - second

        if diff in lines:
            res = first * second * diff
            print("%s * %s * %s = %s" % (first, second, diff, res))
            break

    if res is not 0:
        break

print('part 2 done')
