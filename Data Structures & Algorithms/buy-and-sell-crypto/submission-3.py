class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # keep track of lowest so far
        # if next is greater add as a pair
        # if next is greater than pair, replace
        # if less than or equal, skip
        
        profit = 0
        m = prices[0]

        for i in prices:
            if prices and i < m:
                m = i
            if prices and i - m > profit: 
                profit = i - m

        return profit
            
