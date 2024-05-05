class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [[1,2,3],
        # [4,5,6],
        # [7,8,9]]

        # Transpose
        # [[1,4,7],
        # [2,5,8],
        # [3,6,9]]
        for i in range(len(matrix)):
            for j in range(i):
                    matrix[i][j] ,matrix[j][i] = matrix[j][i], matrix[i][j]

        # Flip
        # [[7,4,1],
        # [8,5,2],
        # [9,6,3]]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j] , matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
