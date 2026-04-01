# Understand find all the unique triplets that add to zero
# Plan
# init result array
# sort nums array
# loop though from first elem to third last elem
    # if elem is a duplicate skip
    # init left pointer to elem next to current elem
    # init right pointer to last elem in array
    # while left < right
        # while left points to duplicate
            # inc left
        # while right points to duplicate
            # dec right 
        # if sum equal zero
            #append idicies to array
            # inc left
            # dec right
        # else if sum greater than zero
            # dec right
        # else
            # inc left
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
        return result
            
        