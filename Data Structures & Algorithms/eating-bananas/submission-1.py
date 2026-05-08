class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            s = l + (r-l)//2
            totalTime=0
            for p in piles:
                totalTime += math.ceil(p/s)
            if totalTime <= h:
                res = s
                r = s - 1
            else:
                l = s + 1
        return res
            