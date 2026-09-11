# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        for i in range(len(pairs)):
            if i == 0:
                pass
            else:
                cur = i
                while cur > 0:
                    temp = pairs[cur-1]
                    if pairs[cur].key >= pairs[cur-1].key:
                        break 
                    pairs[cur-1] = pairs[cur]
                    pairs[cur] = temp
                    cur -= 1
            result.append(pairs[:])
        return result