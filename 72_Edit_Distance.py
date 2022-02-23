class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        
        if m == 0 or n == 0:
            return m + n
        
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = i
        
        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                      dp[i - 1][j],
                                      dp[i][j - 1])
        
        return dp[n][m]
        
        
    def minDistance2(self, word1, word2):
        if word1 is None:
            return len(word2)
        
        if word2 is None:
            return len(word1)
        
        costMap = {}
        
        def minEditDistance(i, j):
            if (i, j) in costMap:
                return costMap[(i, j)]
            
            if i == len(word1):
                costMap[(i, j)] = len(word2) - j
                return costMap[(i, j)]
            
            if j == len(word2):
                costMap[(i, j)] = len(word1) - i                
                return costMap[(i, j)]
            
            if word1[i] == word2[j]:
                return minEditDistance(i + 1, j + 1)
            
            insertCost = 1 + minEditDistance(i, j + 1)
            deleteCost = 1 + minEditDistance(i + 1, j)
            replaceCost = 1 + minEditDistance(i + 1, j + 1)
            
            costMap[(i, j)] = min(insertCost, deleteCost, replaceCost)
            return costMap[(i, j)]
        
        return minEditDistance(0, 0)
        
        
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 is None:
            return len(word2)
        
        if word2 is None:
            return len(word1)
        
        def minEditDistance(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return minEditDistance(i + 1, j + 1)
            
            insertCost = 1 + minEditDistance(i, j + 1)
            deleteCost = 1 + minEditDistance(i + 1, j)
            replaceCost = 1 + minEditDistance(i + 1, j + 1)
            
            return min(insertCost, deleteCost, replaceCost)
        
        return minEditDistance(0, 0)
        