class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_char = ord("a")
        temp = [0] * 26
        res = defaultdict(list)
        
        for string in strs:
            copy = temp.copy()
            for s in string:
                copy[ord(s) - a_char] += 1
            res[tuple(copy)].append(string)
        return [x for x in res.values()]