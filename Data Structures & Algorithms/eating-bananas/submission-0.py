import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles) # edge case

        l, r = 1, max(piles) 

        k = r

        while l <= r:

            mid = (l + r) // 2

            total = 0
            for pile in piles:
                
                total += math.ceil(pile/mid)

            if total > h:
                l = mid + 1 # increase eating rate
            else:
                k = min(k, mid) # decrease eating rate to see other min option

                r = mid - 1

        return k