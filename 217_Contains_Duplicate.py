class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        
        for ele in nums:
            if ele in numsSet:
                return True
            numsSet.add(ele)
            
        return False
        