# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    return any(target in row for row in matrix)
    

print(searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
print(searchMatrix(matrix=[[1],[3]], target=3))