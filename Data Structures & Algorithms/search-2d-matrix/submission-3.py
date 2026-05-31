class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                break
            else:
                continue
        for j in range(len(matrix[i])):
            print(i,j,matrix[i][j])
            if matrix[i][j] == target:
                return True
            else:
                continue
        return False