class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break
        
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            middle = (l + r)//2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        return False