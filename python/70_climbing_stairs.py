class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for step in range(2, n + 1):
            dp.append(dp[step - 2] + dp[step - 1])

        return dp[n]