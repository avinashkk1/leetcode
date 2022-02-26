class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterEleNums2 = {}
        stack = []
        
        for ele in nums2:
            while stack and ele > stack[-1]:
                nextGreaterEleNums2[stack[-1]] = ele
                stack.pop()
            
            stack.append(ele)
        
        nextGreaterEleNums1 = []
        for ele in nums1:
            if ele in nextGreaterEleNums2:
                nextGreaterEleNums1.append(nextGreaterEleNums2[ele])
            else:
                nextGreaterEleNums1.append(-1)
        
        return nextGreaterEleNums1
            
            