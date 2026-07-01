class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            p[i] = p[i-1] * nums[i]
        s = [nums[-1]] *len(nums)
        for i in range(len(nums)-2, -1, -1):
            s[i] = nums[i] * s[i + 1]
        res = [s[1]] *len(nums)
        res[-1] = p[-2]
        for i in range(1, len(nums)-1):
            res[i] = p[i-1] * s[i+1]
        return res