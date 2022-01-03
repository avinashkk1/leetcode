class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        sumSet = set()
        
        while True:
            sumVal = 0
            for ch in num:
                sumVal += (int(ch) * int(ch))
                
            if sumVal == 1:
                return True
            
            if sumVal in sumSet:
                return False
            sumSet.add(sumVal)
            num = str(sumVal)
                
        