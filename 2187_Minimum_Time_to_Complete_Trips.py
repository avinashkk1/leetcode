class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 0
        high = totalTrips * time[0]
        
        def calculateTrips(timeAvailable):
            noOfTrips = 0
            for timeReq in time:
                noOfTrips += (timeAvailable // timeReq)
            return noOfTrips
        
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            tripsPossible = calculateTrips(mid)
            if tripsPossible >= totalTrips:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
            
        