class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0 , len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) //2
            if matrix[row][0] > target:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        for i in matrix[row]:
            if i == target:
                return True
            else:
                continue
        return False