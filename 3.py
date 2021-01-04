from math import ceil
from input import get

print('starting...')

text = get(3)
lines = text.splitlines()

print('working...')

def slider(right: int, down: int, slopelines):
    slope = []
    slope[:] = slopelines
    coords = [0, 0]
    trees = 0
    height = len(slope)
    width = len(slope[0])

    folds = ceil((height * right) / width)
    for l in range(len(slope)):
        slope[l] = slope[l] * folds

    while coords[1] < (height - 1):
        coords[0] += right
        coords[1] += down
        row = coords[1]
        col = coords[0]

        if slope[row][col] == '#':
            trees += 1

    return trees

###
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
###

first = slider(1, 1, lines)
second = slider(3, 1, lines)
third = slider(5, 1, lines)
fourth = slider(7, 1, lines)
fifth = slider(1, 2, lines)
result = first * second * third * fourth * fifth

print('results: %s * %s * %s * %s * %s = %s' % (first, second, third, fourth, fifth, result))

print('done')
