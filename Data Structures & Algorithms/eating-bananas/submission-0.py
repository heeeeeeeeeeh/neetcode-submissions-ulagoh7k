class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minS = r
        while l <= r:
            s = l + (r-l)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile / s)
            
            if time <= h:
                minS = min(minS, s)
                r = s - 1
            else:
                l = s + 1
        return minS
