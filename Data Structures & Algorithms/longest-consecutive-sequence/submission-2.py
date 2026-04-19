class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for i, num in enumerate(nums):
            if num-1 in numSet:
                continue

            j = i + 1
            length = 1
            prevNum = num
            while prevNum + 1 in numSet:
                prevNum = prevNum + 1
                j += 1
                length += 1
            maxLen = max(maxLen, length)
        return maxLen
            