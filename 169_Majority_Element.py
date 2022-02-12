class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rank = 0
        
        for ele in nums:
            if rank == 0:
                candidate = ele
            if candidate == ele:
                rank += 1
            else:
                rank -= 1
        
        return candidate
        
        