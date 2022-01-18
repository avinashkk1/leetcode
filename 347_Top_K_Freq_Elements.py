import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = {}
        for ele in nums:
            if ele in numsFreq:
                numsFreq[ele] += 1
            else:
                numsFreq[ele] = 1
                
        topkFreq = []
        heapq.heapify(topkFreq)
        
        for ele, freq in numsFreq.items():
            heapq.heappush(topkFreq, (freq, ele))
            if len(topkFreq) > k:
                heapq.heappop(topkFreq)
        
        return [ele[1] for ele in topkFreq]
        
        
        