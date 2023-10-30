''' Sliding window algorithm. '''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        l = 0 # Current left price.
        r = 1 # Current right price.

        while r < len(prices):
            if prices[r] > prices[l]: # If the right price is higher.
                
                # This guarantees that the max profit between the current left price and current right price is found. 
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            else: # If the right price is not higher.
                l = r # Since the max profit between the current left price and current right price is found, and now we've found a new low price which is the current right price, so we can go ahead set the new low price as the current left price to find the following potential max profit.
            r += 1 # Always check the next right price.
        
        return maxP