class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = min(heights[0], heights[-1]) * (len(heights) - 1)
        print(res)
        i, j = 0, len(heights) - 1
        while i < j:
            print(heights[i], heights[j], j-i)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            res = max(res, (j-i) * min(heights[i], heights[j]))
        return res
            