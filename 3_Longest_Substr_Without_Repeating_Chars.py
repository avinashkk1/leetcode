class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charLoc = {}
        longestSubstrLen = 0
        startIndex = 0
        
        for i, ch in enumerate(s):
            if ch in charLoc:
                startIndex = max(startIndex, charLoc[ch] + 1)
            charLoc[ch] = i
            longestSubstrLen = max(longestSubstrLen, i - startIndex + 1) 
        
        return longestSubstrLen
    
                
        