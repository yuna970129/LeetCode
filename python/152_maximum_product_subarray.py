class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [n for n in nums]
        min_dp = [n for n in nums]

        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i], max_dp[i - 1] * nums[i])

        return max(max_dp)