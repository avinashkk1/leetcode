class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        nums1Freq = {}
        for ele in nums1:
            if ele in nums1Freq:
                nums1Freq[ele] += 1
            else:
                nums1Freq[ele] = 1
        
        ans = []
        for ele in nums2:
            if ele in nums1Freq and nums1Freq[ele] > 0:
                nums1Freq[ele] -= 1
                ans.append(ele)                
        
        return ans
            
        