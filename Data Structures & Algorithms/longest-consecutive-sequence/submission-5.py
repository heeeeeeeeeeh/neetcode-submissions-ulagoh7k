class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxL = 0

        for num in n:
            if num-1 in n:
                continue
            
            length = 1
            prev = num
            while prev + 1 in n:
                length += 1
                prev = prev + 1
            maxL = max(maxL, length)
        return maxL