class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxconsecutive = 0
        chars = set(s)
        # check which char has longest cons
        for i in chars:
            # init value for consecutive
            l = count = 0
            for r in range(len(s)):
                # check how many count there is rn
                if s[r] == i:
                    count += 1
                # length of consecutive minus the exchangeable
                while (r - l + 1) - count > k:
                    # check if previous l is the char
                    if s[l] == i:
                        # if yes then remove one count, since it is not consecutive anymore
                        count -= 1
                    # expand l
                    l += 1
                maxconsecutive = max(maxconsecutive, r-l+1)
        return maxconsecutive