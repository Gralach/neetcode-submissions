class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict_s = {}
        anagram_dict_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in anagram_dict_s:
                anagram_dict_s[s[i]] = 1
            elif s[i] in anagram_dict_s:
                anagram_dict_s[s[i]] += 1     

            if t[i] not in anagram_dict_t:
                anagram_dict_t[t[i]] = 1
            elif t[i] in anagram_dict_t:
                anagram_dict_t[t[i]] += 1

        if anagram_dict_s == anagram_dict_t:
            return True

        else:
            return False