
#Understand: return the length of the longest sequence of numbers that are in the array
#Plan: create hash set from list
# if array length is zero return 0
# set max length to 1
#Loop though each elem in list
    # if current num-1 exits in set
        # set prev num to current num
        # set length of sequence to two
        # loop from current number+1 to end of list
            # if current number equal prev num + 1
                # set prev num to current num
                # increment length of sequence by on
        # if length of sequence greater than max sequence
            # set max sequence to length of sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        maxLen = 1
        n = set(nums)
        for num in n:
            if num-1 not in n:
                curLen = 1
                prevNum = num
                while prevNum+1 in n:
                    curLen += 1
                    prevNum += 1
                maxLen = max(curLen,maxLen)
        return maxLen