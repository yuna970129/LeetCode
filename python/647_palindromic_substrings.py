class Solution:
    def countSubstrings(self, s: str) -> int:
        def cal_pal(start, end):
            while (start-1) >= 0 and (end+1) < len(s):
                if s[start-1] == s[end+1]:
                    start -= 1
                    end += 1
                else:
                    break
            return (end-start+1)//2

        cand = []
        pal_cnt = len(s)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cand.append((i,i+1))
            if (i+2) < len(s):
                if s[i] == s[i+2]:
                    cand.append((i,i+2))
        
        for start, end in cand:
            pal_cnt += cal_pal(start, end)

        return pal_cnt
