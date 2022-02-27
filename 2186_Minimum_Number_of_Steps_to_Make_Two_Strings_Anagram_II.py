import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_c = collections.Counter(s)
        t_c = collections.Counter(t)
        
        count = 0
        # print(s_c)
        for key, value in s_c.items():
            if key in t_c:
                count += abs(s_c[key] - t_c[key])
            else:
                count += value
                
        for key, value in t_c.items():
            if key not in s_c:
                count += value
        
        return count
        