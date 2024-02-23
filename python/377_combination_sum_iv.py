class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target):
            for n in nums:
                print(i,n,target)
                if (i+n) <= target:
                    dp[i+n] += dp[i]
        return dp[-1]
