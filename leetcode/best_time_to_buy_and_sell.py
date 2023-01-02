class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        for i in range(0, len(prices) - 1):
            if len(prices[i + 1: len(prices) - 1]) > 0:
                p = max(prices[i + 1: len(prices) - 1]) - prices[i]
                print(p, prices[i])
                if p > profit:
                    profit = p
            
        return profit

s = Solution()
print(s.maxProfit([1,2]))
