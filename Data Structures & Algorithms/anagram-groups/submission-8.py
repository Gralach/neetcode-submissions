class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = ord("a")
        res = defaultdict(list)
        for string in strs:
            temp = [0] * 26
            for char in string:
                temp[ord(char)-a] +=1
            res[tuple(temp)].append(string)
        return(list(res.values()))