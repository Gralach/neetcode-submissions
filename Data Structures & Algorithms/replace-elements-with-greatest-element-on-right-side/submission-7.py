class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp, res = 0, [0] * len(arr)
        for i in range(len(arr) -1 , -1 , -1):
            if i == len(arr)-1:
                res[i] = -1
            else:
                res[i] = temp
            temp = max(temp, arr[i])
        return res