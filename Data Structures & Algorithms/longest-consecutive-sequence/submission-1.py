class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 0

        for n in numSet:
            if n - 1 in numSet:
                continue
            
            length = 1
            while n + length in numSet:
                length += 1
            maxL = max(maxL, length)

        return maxL