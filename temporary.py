# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
"""
You are given an m x n grid where each cell can have one of three values:
* 0 representing an empty cell,
* 1 representing a fresh apple, or
* 2 representing a rotten apple.
Every minute, any fresh apple that is 4-directionally adjacent to a rotten apple becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh apple. If this is impossible, return -1.
 
[0,1,1]
[1,0,0]
[0,1,2]

"""
print("Hello, world!")

def rotten_apple_func(apple_grid):
    bfs_queue = list()
    minutes_to_rot = 0
    for ind1, row in enumerate(apple_grid):
        for ind2 in range(len(row)):
            if apple == 2:
                bfs_queue.insert(0,tuple(ind1,ind2))
    
    temp_list = list()
    while len(bfs_queue) > 0:
        i1, i2 = bfs_queue.pop()
        if apple_grid[i1-1][i2] == 1:
            apple_gird[i1-1][i2] = 2
            temp_list.append(tuple(i1-1,i2))
        if apple_grid[i1][i2-1] == 1:
            apple_gird[i1][i2-1] = 2
            temp_list.append(tuple(i1,i2-1))
        if apple_grid[i1+1][i2] == 1:
            apple_gird[i1+1][i2] = 2
            temp_list.append(tuple(i1+1,i2))
        if apple_grid[i1][i2+1] == 1:
            apple_gird[i1][i2+1] = 2
            temp_list.append(tuple(i1,i2+1))
