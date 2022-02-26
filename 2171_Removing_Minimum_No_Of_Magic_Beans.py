class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        totalBeans = sum(beans)
        minBeansToRemove = float('inf')
        n = len(beans)
        
        for i in range(n):
            minBeansToRemove = min(minBeansToRemove, totalBeans - ((n - i) * beans[i]))
        
        return minBeansToRemove
            
        
        
    def minimumRemoval1(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        ans = float('inf')
        for i in range(n):
            currSum = 0
            for j in range(n):
                if beans[j] < beans[i]:
                    currSum += beans[j]
                else:
                    currSum += (beans[j] - beans[i])
            
            ans = min(ans, currSum)
        
        return ans
                
                
        