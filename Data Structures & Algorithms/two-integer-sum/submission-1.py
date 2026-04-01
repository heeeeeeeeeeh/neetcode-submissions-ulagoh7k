class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousDiff = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in previousDiff:
                return [previousDiff[diff], i]
            else:
                previousDiff[num] = i