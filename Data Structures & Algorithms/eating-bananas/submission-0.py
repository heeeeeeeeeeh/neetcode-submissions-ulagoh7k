class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minS = 0
        
        while l <= r:
            k = l + (r-l)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            
            if time <= h:
                minS = k
                r = k - 1
            else:
                l = k + 1
        return minS
