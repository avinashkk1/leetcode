class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = 0
        last_seated_index = -1
        
        i = 0
        while i < n:
            if seats[i] == 1:
                if last_seated_index == -1:
                    max_dist = max(max_dist, i)
                else:
                    max_dist = max(max_dist, (i - last_seated_index) // 2)
                last_seated_index = i
            i += 1
        
        if seats[n - 1] == 0:
            max_dist = max(max_dist, n - 1 - last_seated_index)
        
        return max_dist
        
        
    
                
        