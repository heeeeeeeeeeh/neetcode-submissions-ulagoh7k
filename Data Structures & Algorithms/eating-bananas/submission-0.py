class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minS = r
        while l <= r:
            mid = l + (r-l)//2 

            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time <= h:
                minS = mid
                r = mid - 1
            else:
                l = mid + 1
        return minS
