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

# i = len(grid)
x = 0
# print i
while True:
    # for x in range(len(grid[0] - 1):

    for i in range(len(grid)):
        print (grid[i][x], end=' ')

    x = x + 1

    print (end='\n')

    if x > len(grid):
        break

        # print (grid[0][i], grid[1][i], grid[2][i], grid[3][i], grid[4][i], grid[5][i], grid[6][i], grid[7][i], grid[8][i])
