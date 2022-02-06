class Solution:
    def climbStairs1(self, n: int) -> int:
        # Brute force
        return self.climbStairsRec(0, n)
    
    def climbStairsRec(self, index, n):
        
        
        if index == n:
            return 1
        
        return self.climbStairsRec(index + 1, n) + self.climbStairsRec(index + 2, n)
    
    def climbStairs(self, n: int) -> int:
        # With memoization
        noOfWays = [None] * (n + 1)
        noOfWays[n] = 1
        self.climbStairsWithMemoization(noOfWays, 0, n)
        return noOfWays[0]
        
    def climbStairsWithMemoization(self, noOfWays, index, n):
        if index > n:
            return 0
        
        if noOfWays[index] is not None:
            return noOfWays[index]
    
        noOfWays[index] = self.climbStairsWithMemoization(noOfWays, index + 1, n) + self.climbStairsWithMemoization(noOfWays, index + 2, n)
        
        return noOfWays[index]
        
        
        
        
        
    
    
        