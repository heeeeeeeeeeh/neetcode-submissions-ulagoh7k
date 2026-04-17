class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        sufix = [nums[-1]] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            sufix[i] = nums[i] * sufix[i+1]

        
        res = [sufix[1]]*len(nums)
        res[-1] = prefix[-2]

        for i in range(1,len(nums)-1):
            res[i] = prefix[i-1] * sufix[i+1]
        return res