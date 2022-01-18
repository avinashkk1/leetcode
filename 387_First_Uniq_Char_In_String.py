class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        for ch in s:
            if ch in charDict:
                charDict[ch] += 1
            else:
                charDict[ch] = 1
        
        for i, ch in enumerate(s):
            if charDict[ch] == 1:
                return i
        
        return -1
        