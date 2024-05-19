class Solution:
    def longestPalindrome(self, s: str) -> str:
        def cal_len(start, end):
            while (start-1) >= 0 and (end+1) < len(s):
                if s[start-1] == s[end+1]:
                    start -= 1
                    end += 1
                else:
                    break
            return (end-start+1), s[start:end+1]

        cand = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cand.append((i,i+1))
            if (i+2) < len(s):
                if s[i] == s[i+2]:
                    cand.append((i,i+2))
        
        max_len = 1
        max_pal = s[0]
        for start, end in cand:
            length, pal = cal_len(start, end)
            if max_len < length:
                max_len = length
                max_pal = pal

        return max_pal
