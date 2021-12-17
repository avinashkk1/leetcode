class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        negSignFlag = True if num < 0 else False
        
        num = abs(num)
        base7_str = ''
        while num > 0:
            base7_str += str(num % 7)
            num = num // 7
        
        base7_str = base7_str[::-1]
        if negSignFlag:
            return '-' + base7_str
        
        return base7_str
            
        