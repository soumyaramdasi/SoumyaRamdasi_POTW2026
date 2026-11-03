class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        #initially, 
        empty = numBottles
        total = numBottles

        while empty >= numExchange:

            empty = empty - numExchange
            empty = empty + 1
            total = total + 1
        
        return total
