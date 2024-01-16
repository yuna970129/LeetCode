class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fw = [1]*len(nums)
        rv = [1]*len(nums)
        for i in range(len(nums)-1):
            fw[i+1] = fw[i]*nums[i]
            rv[len(nums)-i-2] = rv[len(nums)-i-1]*nums[len(nums)-i-1]
        ans = []
        for i in range(len(nums)):
            ans.append(fw[i]*rv[i])

        return ans