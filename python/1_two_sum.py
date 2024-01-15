class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints = dict()
        for i, n in enumerate(nums):
            ints[n] = i

        for i, n in enumerate(nums):
            if (target - n) in ints and i != ints[target - n]:
                return [i, ints[target - n]]