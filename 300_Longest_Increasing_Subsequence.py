class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 1:
            return 0
        
        seq = [nums[0]]
        for ele in nums[1:]:
            if ele > seq[-1]:
                seq.append(ele)
            else:
                index = self.getInsertPos(seq, ele)
                seq[index] = ele
        
        return len(seq)
    
    def getInsertPos(self, nums, ele):
        n = len(nums)
        lo = 0
        hi = n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > ele:
                hi = mid - 1
            elif nums[mid] < ele:
                lo = mid + 1
            else:
                return mid
        
        return lo if lo < n else lo - 1
        
        
        
        
        
        
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        