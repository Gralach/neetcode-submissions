class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, lists):
            index = l - (l-r)//2
            print(index)
            if l > r:
                return -1
            elif lists[index] == target:
                return index
            elif lists[index] > target:
                return binary_search(l , index - 1, lists)
            else:
                return binary_search(index + 1, r, lists)

        l = 0
        r = len(nums) - 1
        return binary_search(l, r, nums)