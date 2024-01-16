class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [num for num in nums]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)