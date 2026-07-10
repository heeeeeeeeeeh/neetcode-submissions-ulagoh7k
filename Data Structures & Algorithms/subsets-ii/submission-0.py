class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            res.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
        dfs(0)
        return res