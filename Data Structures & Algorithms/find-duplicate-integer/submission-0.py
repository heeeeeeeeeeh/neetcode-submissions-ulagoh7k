class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        left = 0
        while left != slow:
            slow = nums[slow]
            left = nums[left]
        return left