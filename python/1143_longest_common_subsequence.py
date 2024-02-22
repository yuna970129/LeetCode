class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0]*(len(text1)+1)
        for i in range(1,len(text2)+1):
            cnt = 0
            for j in range(1,len(text1)+1):
                if cnt < dp[j]:
                    cnt = dp[j]
                elif (text2[i-1] == text1[j-1]):
                    dp[j] = cnt+1
        return max(dp)
