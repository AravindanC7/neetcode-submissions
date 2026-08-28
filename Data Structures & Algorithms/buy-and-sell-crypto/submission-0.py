class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=None
        profit=0
        for x in prices:
            if buy == None:
                buy = x
                continue
            if x<=buy:
                buy=x
            else:
                new_profit =x-buy
                profit = max(profit,new_profit)
        return profit

        