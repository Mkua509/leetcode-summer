class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        # Sell in for sell in prices: is the value at the current index not the index
        for sell in prices:
            maxProfit = max(maxProfit, sell - minPrice)
            minPrice = min(minPrice, sell)
        
        return maxProfit