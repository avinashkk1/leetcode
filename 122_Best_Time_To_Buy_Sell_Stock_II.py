class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            profit += (max(0, prices[i] - prices[i - 1]))
        
        return profit
    
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n < 2:
            return 0
        
        profit = 0
        i = 0
        
        while True:
            while i + 1 < n and prices[i] > prices[i + 1]:
                i += 1
            
            if i >= n:
                break
            
            local_min = prices[i]
            
            while i + 1 < n and prices[i + 1] > prices[i]:
                i += 1
            
            if i >= n:
                break
            
            local_max = prices[i]
            profit += (local_max - local_min)
            i += 1
        
        return profit
            
            
        