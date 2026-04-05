class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in seen:
                return [min(seen[diff], i), max(i, seen[diff])]
            seen[nums[i]] = i