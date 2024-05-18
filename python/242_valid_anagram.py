from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        ss = defaultdict(int)
        tt = defaultdict(int)

        for i in range(len(s)):
            ss[s[i]] += 1
            tt[t[i]] += 1

        return ss == tt
