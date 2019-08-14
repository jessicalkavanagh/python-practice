import numpy as np 

## TASK 2
# given a 5x5 grid, add the last column and row, then flip the card at the
# # coordinate specified by the user
five_by_five_grid = [
['X','0','X','X','X'],
['X','X','0','0','0'],
['X','0','X','0','X'],
['0','X','X','X','X'],
['X','0','0','X','X'],
]
# first step is to add colum 6 and row 6
add_column = np.array(['X','0','X','0','X'])
six_by_five_grid =  np.column_stack((five_by_five_grid, add_column))

add_row = np.array(['X','0','X','0','X','0'])
six_by_six_grid =  np.row_stack((six_by_five_grid, add_row))

print(np.count_nonzero(six_by_six_grid == 1))

# def flip_user(x,y):
#     for line in six_by_six_grid: print(line)
#     print()
#     if six_by_six_grid[x][y] == 'X':
#         six_by_six_grid[x][y] = '0'
#     else:
#         six_by_six_grid[x][y] = 'X'
#     print('This is the new grid')
#     for line in six_by_six_grid: print(line)
#     print('The coordinate of the card that was flipped is',x,y)    
# flip_user(0,2)



# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
# output the grid with the flipped card
## TASK 2

# given a six by six grid, work out what card was flipped
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)