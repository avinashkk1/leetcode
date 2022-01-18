class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n < 3:
            return []
        
        nums.sort()
        
        if nums[0] > 0:
            return []
        
        triplets = set()
        
        for i, ele in enumerate(nums):
            twoSumSets = self.twoSum(nums[i + 1:], -1 * ele)
            for twoSumSet in twoSumSets:
                triplets.add((ele, ) + twoSumSet)        
        
        triplets = [list(triplet) for triplet in triplets]
        
        return triplets
    
    def twoSum(self, nums, target):
        n = len(nums)
        
        if n < 2:
            return set()
        
        i = 0
        j = n - 1
        
        ans = set()
        
        while i < j:
            if nums[i] + nums[j] == target:
                ans.add((nums[i], nums[j]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        
        return ans
            
                
            
            
            
            
        