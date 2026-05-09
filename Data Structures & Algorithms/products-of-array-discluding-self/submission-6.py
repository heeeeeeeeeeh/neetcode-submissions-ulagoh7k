class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        sufix = [nums[-1]] * len(nums)
        res = []

        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(sufix)-2,-1,-1):
            sufix[i] = sufix[i+1] * nums[i]

        res = [sufix[1]]*len(nums)
        res[-1] = prefix[-2]

        for i in range(1,len(nums)-1):
            res[i] = sufix[i+1] * prefix[i-1]
        return res