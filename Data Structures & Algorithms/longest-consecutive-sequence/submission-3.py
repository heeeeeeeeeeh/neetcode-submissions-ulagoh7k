class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxL = 0

        for num in numsSet:
            if num-1 in numsSet:
                continue
            length = 1
            prevNum = num
            while prevNum + 1 in numsSet:
                length += 1
                prevNum += 1
            maxL = max(maxL,length)
        return maxL