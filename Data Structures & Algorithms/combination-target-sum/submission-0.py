class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        nums.sort()
        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + sum > target:
                    return
                subset.append(nums[j])
                dfs(j, nums[j] + sum)
                subset.pop()
        dfs(0, 0)
        return res