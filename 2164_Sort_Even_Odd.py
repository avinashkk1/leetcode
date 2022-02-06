class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        oddList = []
        evenList = []
        
        for i in range(n):
            if i % 2 == 0:
                evenList.append(nums[i])
            else:
                oddList.append(nums[i])
        
        evenList.sort()
        oddList.sort()
        
        #print(evenList)
        #print(oddList)
        
        j = 0
        k = len(oddList) - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = evenList[j]
                j += 1
            else:
                nums[i] = oddList[k]
                k -= 1
        
        return nums
            
            