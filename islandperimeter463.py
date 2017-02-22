def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                if j - 1 >= 0:
                    if grid[i][j-1] == 0:
                        m += 1
                if j - 1 < 0:
                        m += 1
                if j + 1 < len(grid):
                    if grid[i][j+1] == 0:
                        m += 1
                if j + 1 >= len(grid):
                        m += 1
                if i - 1 >= 0:
                    if grid[i-1][j] == 0:
                        m += 1
                if i - 1 < 0:
                        m += 1
                if i + 1 < len(grid):
                    if grid[i+1][j] == 0:
                        m += 1
                if i + 1 >= len(grid):
                        m += 1
    return m
islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])

# class Solution(object):
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     if j - 1 >= 0:
#                         if grid[i][j-1] == 0:
#                             m += 1
#                     if j - 1 < 0:
#                             m += 1
#                     if j + 1 < len(grid[0]):
#                         if grid[i][j+1] == 0:
#                             m += 1
#                     if j + 1 >= len(grid[0]):
#                             m += 1
#                     if i - 1 >= 0:
#                         if grid[i-1][j] == 0:
#                             m += 1
#                     if i - 1 < 0:
#                             m += 1
#                     if i + 1 < len(grid):
#                         if grid[i+1][j] == 0:
#                             m += 1
#                     if i + 1 >= len(grid):
#                             m += 1
#         return m