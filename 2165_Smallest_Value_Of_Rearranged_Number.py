class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        digitFreq = {}
        
        numString = str(num)
        if num < 0:
            numString = numString[1:]

        for ch in numString:
            if ch not in digitFreq:
                digitFreq[ch] = 1
            else:
                digitFreq[ch] += 1
        
        ansStr = ''
        
        if num > 0:
            for i in range(1, 10):
                ch = str(i)
                if ch in digitFreq:
                    ansStr += ch
                    digitFreq[ch] -= 1
                    break
            
            for i in range(10):
                ch = str(i)
                if ch in digitFreq:
                    ansStr += (ch * digitFreq[ch])
        else:
            ansStr += '-'
            for i in range(9, -1, -1):
                ch = str(i)
                if ch in digitFreq:
                    ansStr += (ch * digitFreq[ch])
        
        return int(ansStr)
                

            
                

            
        