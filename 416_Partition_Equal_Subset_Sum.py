class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Brute force with memoization
        numsSum = sum(nums)
        
        if numsSum % 2 == 1:
            return False
        
        subSetSum = numsSum // 2
        subSetSumMap = {}
        
        def findSubSetSum(subSetSum, index):
            if (subSetSum, index) in subSetSumMap:
                return subSetSumMap[(subSetSum, index)]
            
            if subSetSum == 0:
                subSetSumMap[(subSetSum, index)] = True
                return True
            
            if subSetSum < 0:
                subSetSumMap[(subSetSum, index)] = False
                return False
            
            if index < 0:
                subSetSumMap[(subSetSum, index)] = False
                return False
            
            subSetSumMap[(subSetSum, index)] = findSubSetSum(subSetSum - nums[index], index - 1) or findSubSetSum(subSetSum, index - 1)
            return subSetSumMap[(subSetSum, index)]
            
        
        return findSubSetSum(subSetSum, len(nums) - 1)
        
    
    def canPartition1(self, nums: List[int]) -> bool:
        # Brute force, TLE
        numsSum = sum(nums)
        
        if numsSum % 2 == 1:
            return False
        
        subSetSum = numsSum // 2
        
        def findSubSetSum(subSetSum, index):
            if subSetSum == 0:
                return True
            
            if subSetSum < 0:
                return False
            
            if index < 0:
                return False
            
            return findSubSetSum(subSetSum - nums[index], index - 1) or findSubSetSum(subSetSum, index - 1)
            
        
        return findSubSetSum(subSetSum, len(nums) - 1)
        