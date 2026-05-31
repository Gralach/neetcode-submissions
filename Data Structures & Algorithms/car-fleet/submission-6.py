class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        check = [(p,s) for p, s in zip(position, speed)]
        check.sort(reverse=True)
        result = []
        print(check)
        for pos,spe in check:
            result.append((target-pos)/spe)
            if (len(result) >= 2) and (result[-1] <= result[-2]):
                result.pop()
            print(result)
        return len(result)