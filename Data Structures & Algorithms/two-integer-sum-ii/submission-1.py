#Understand: find two numbers in array that add up to target and return their index
#Plan:
# init left pointer to first elem
# init right pointer to last elem
# while left pointer is less than right pointer
    # if sum of elements at pointers are equal to target
        # return pointers (1-indexed)
    # else if sum of elements at pointers is greater than index
        # dec right pointer
    # else
        # inc left pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1
            else:
                left +=1