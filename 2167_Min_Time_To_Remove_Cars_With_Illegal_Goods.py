class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        if n == 1:
            if s[0] == '0':
                return 0
            return 1
        
        timeTakenByLeftPass = [0] * n
        if s[0] == '1':
            timeTakenByLeftPass[0] = 1
        for i in range(1, n):
            if s[i] == '1':
                timeTakenByLeftPass[i] = min(i + 1, timeTakenByLeftPass[i - 1] + 2)
            else:
                timeTakenByLeftPass[i] = timeTakenByLeftPass[i - 1]

        timeTakenByRightPass = [0] * n
        if s[n - 1] == '1':
            timeTakenByRightPass[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                timeTakenByRightPass[i] = min(n - i, timeTakenByRightPass[i + 1] + 2)
            else:
                timeTakenByRightPass[i] = timeTakenByRightPass[i + 1]

        minTime = timeTakenByLeftPass[0] + timeTakenByRightPass[1]
        for i in range(n - 1):
            minTime = min(minTime, timeTakenByLeftPass[i] + timeTakenByRightPass[i + 1])
        
        return minTime
            
        
        
        
        
        