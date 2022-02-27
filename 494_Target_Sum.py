class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        targetSumWaysMap = {}
        
        def isTargetSum(totalTillNow, index):
            if index == len(nums):
                return 1 if totalTillNow == target else 0
            
            if (totalTillNow, index) in targetSumWaysMap:
                return targetSumWaysMap[(totalTillNow, index)]
            
            targetSumWaysMap[(totalTillNow, index)] = isTargetSum(totalTillNow + nums[index], index + 1) + isTargetSum(totalTillNow - nums[index], index + 1)
            
            return targetSumWaysMap[(totalTillNow, index)]
        
        return isTargetSum(0, 0)
        