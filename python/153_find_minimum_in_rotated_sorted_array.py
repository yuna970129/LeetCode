class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]