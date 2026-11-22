class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 0

        while numSet:
            num = numSet.pop()
            length = 1
            while num + 1 in numSet:
                num += 1
                length += 1
                numSet.remove(num)
            num -= length
            while num in numSet:
                length += 1
                numSet.remove(num)
                num -= 1
            maxL = max(maxL, length)
        return maxL