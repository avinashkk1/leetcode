class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        j = n - 1
        k = n - 1
        sortedSquares = [0] * n
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                sortedSquares[k] = nums[i] * nums[i]
                i += 1
            else:
                sortedSquares[k] = nums[j] * nums[j]
                j -= 1
            k -= 1
        
        return sortedSquares
            
                
        
        
        
        
    def bsearch_left(self, nums, ele):
        low = 0
        high = len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= ele:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

    def getSquares(self, nums):
        squaredNums = []
        for ele in nums:
            squaredNums.append(ele * ele)
        
        return squaredNums
    
    
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [nums[0] * nums[0]]
    
        firstNegNumIndex = self.bsearch_left(nums, 0)
        
        if firstNegNumIndex == -1:
            return self.getSquares(nums)
        
        if firstNegNumIndex == n:
            return self.getSquares(nums[::-1])
        
        negNumIndex = firstNegNumIndex
        nonNegNumIndex = negNumIndex + 1
        
        sortedSquaredNums = []
        while negNumIndex >= 0 and nonNegNumIndex < n:
            if abs(nums[negNumIndex]) < nums[nonNegNumIndex]:
                sortedSquaredNums.append(nums[negNumIndex] * nums[negNumIndex])
                negNumIndex -= 1
            else:
                sortedSquaredNums.append(nums[nonNegNumIndex] * nums[nonNegNumIndex])
                nonNegNumIndex += 1
        
        while negNumIndex >= 0:
            sortedSquaredNums.append(nums[negNumIndex] * nums[negNumIndex])
            negNumIndex -= 1
        
        while nonNegNumIndex < n:
            sortedSquaredNums.append(nums[nonNegNumIndex] * nums[nonNegNumIndex])
            nonNegNumIndex += 1
        
        return sortedSquaredNums
            
                