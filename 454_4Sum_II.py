class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        nums12Map = {}
        for ele1 in nums1:
            for ele2 in nums2:
                if ele1 + ele2 in nums12Map:
                    nums12Map[ele1 + ele2] += 1
                else:
                    nums12Map[ele1 + ele2] = 1
        
        count = 0
        for ele3 in nums3:
            for ele4 in nums4:
                if -1 * (ele3 + ele4) in nums12Map:
                    count += nums12Map[-1 * (ele3 + ele4)]
        
        return count
                    
                
        