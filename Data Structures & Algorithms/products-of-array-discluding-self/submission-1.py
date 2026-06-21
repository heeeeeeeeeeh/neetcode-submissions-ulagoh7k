class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]] *len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i]
        suf = [nums[-1]] * len(nums)
        for i in range(len(nums)-2, -1,-1):
            suf[i] = nums[i] * suf[i+1]
        res = [suf[1]]*len(nums)
        res[-1] = pre[-2]
        for i in range(1, len(nums)-1):
            res[i] = pre[i-1] * suf[i+1]
        return res
            