class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nth_bit = 1 << n
        powerSet = []
        
        for i in range(2 ** n):
            binString = bin(i | nth_bit)[3:]
            powerSet.append( [nums[j] for j in range(n) if binString[j] == '1'] )
        
        return powerSet
            
        
        
        
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        
        for ele in nums:
            powerSet += [currSet + [ele] for currSet in powerSet]
        
        return powerSet
        