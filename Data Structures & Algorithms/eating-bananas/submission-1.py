import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def testRate(rate):
            hours = 0
            for num in piles:
                hours += math.ceil(num / rate)

            return hours     

        low = 1
        high = max(piles)
        res = high

        while low <= high:
            midpoint = (low + high) // 2

            if testRate(midpoint) <= h:
                res = midpoint
                high = midpoint - 1
            else:
                low = midpoint + 1

        return res

        
        


            
        