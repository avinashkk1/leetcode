class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, ele in enumerate(nums):
            if target - ele in numDict:
                return [i, numDict[target - ele]]
            numDict[ele] = i
            