class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        check1 = defaultdict(int)
        for i in s1:
            check1[i] += 1
        for i in range(len(s2)):
            temp, length = check1.copy(), 0
            while (i + length) < len(s2):
                if(temp[s2[i+length]] == 0):
                    break
                else:
                    temp[s2[i+length]] -=1 
                    # print(temp, sum(temp.values()), i)
                    length += 1
                    if sum(temp.values()) == 0:
                        return True
        return False