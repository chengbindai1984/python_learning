from __future__ import print_function

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0

while True:

    for i in range(len(grid)):
        print (grid[i][x], end=' ')

    x = x + 1

    print (end='\n')

    if x > len(grid[x])-1:
        break

       