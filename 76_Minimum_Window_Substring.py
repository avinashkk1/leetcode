class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if n > m:
            return ""
    
        left = right = 0
        tCharFreq = collections.Counter(t)
        windowCharFreq = defaultdict(int)
        tCharFreqLen = len(tCharFreq)
        count = 0
        ans = (m + 1, left, right)
        
        while right < m:
            
            windowCharFreq[s[right]] += 1
            
            if s[right] in tCharFreq and tCharFreq[s[right]] == windowCharFreq[s[right]]:
                count += 1
            
            while left <= right and count == tCharFreqLen:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                windowCharFreq[s[left]] -= 1
                
                if s[left] in tCharFreq and windowCharFreq[s[left]] < tCharFreq[s[left]]:
                    count -= 1
            
                left += 1
            
            right += 1
        
        if ans[0] > m:
            return ""
        
        return s[ans[1]: ans[2] + 1]
                
                
        
        