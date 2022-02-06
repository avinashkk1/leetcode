class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0 or n == 0:
            return m + n
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # print(dp)
        
        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1])
        
        return dp[m][n]
        
        
        
        
        
    def minDistance1(self, word1: str, word2: str) -> int:
        
        def findDist(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return findDist(i + 1, j + 1)
            
            insertDist = findDist(i, j + 1)
            deleteDist = findDist(i + 1, j)
            replaceDist = findDist(i + 1, j + 1)
            
            return 1 + min(insertDist, deleteDist, replaceDist)
        
        return findDist(0, 0)
        