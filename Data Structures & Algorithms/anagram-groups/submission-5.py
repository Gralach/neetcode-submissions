class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            index = [0]*26
            for i in str:
                index[ord(i) - ord("a")]+=1
            groups[tuple(index)].append(str)
        return (list(groups.values()))