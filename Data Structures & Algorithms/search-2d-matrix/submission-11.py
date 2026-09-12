class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length, height = len(matrix[0]) -1, len(matrix)-1

        TOP, BOTTOM = 0, height

        while TOP <= BOTTOM:
            middle_v = (TOP + BOTTOM) //2
            if middle_v > height:
                break
            elif (matrix[middle_v][0] <= target) and (matrix[middle_v][-1] >= target):
                break
            elif matrix[middle_v][-1] > target:
                BOTTOM = middle_v - 1
            elif matrix[middle_v][0] < target:
                TOP = middle_v + 1
        L, R = 0, length
        while L <= R:
            middle_h = (L + R) // 2

            if matrix[middle_v][middle_h] > target:
                R =  middle_h - 1
            elif matrix[middle_v][middle_h] < target:
                L = middle_h + 1
            elif matrix[middle_v][middle_h] == target:
                return True
        return False