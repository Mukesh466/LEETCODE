class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tot = numBottles
        empty = numBottles
        while empty >= numExchange:
            new=empty // numExchange
            tot += new
            empty = (empty % numExchange) + new
        return tot
        
