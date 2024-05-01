### Time Complexity: O(N×M), Space Complexity: O(N+M)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         zr, zc = [], []
#         c, r = len(matrix[0]), len(matrix)
#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j] == 0:
#                     zc.append(j)
#                     zr.append(i)
#         for i in zr:
#             matrix[i] = [0]*c

#         for j in zc:
#             for i in range(r):
#                 matrix[i][j] = 0

### Time Complexity: O(N×M), Space Complexity: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        c, r = len(matrix[0]), len(matrix)
        first_row_zero = any(matrix[i][0] == 0 for i in range(r))
        first_col_zero = any(matrix[0][j] == 0 for j in range(c))

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for i in range(r):
                matrix[i][0] = 0

        if first_col_zero:
            for j in range(c):
                matrix[0][j] = 0 
