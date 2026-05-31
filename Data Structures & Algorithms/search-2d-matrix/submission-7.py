class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) -1
        while top <= bottom:
            row = (top + bottom) //2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0]> target:
                bottom = row - 1
            else:
                break
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            middle = (l+r) //2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                l = middle + 1
            else:
                r = middle -1
        return False
