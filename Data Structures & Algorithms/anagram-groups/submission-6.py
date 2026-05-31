class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            temp = [0]*26
            for char in str:
                temp[ord(char) - ord("a")] += 1
            groups[tuple(temp)].append(str)
        return([x for x in groups.values()])