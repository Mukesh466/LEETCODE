class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        cols = len(matrix[0])
        for i in range(row):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i] , matrix[i][j]

        for k in range(row):
            matrix[k].reverse()        