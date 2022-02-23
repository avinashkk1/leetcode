

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        
        
        left = defaultdict(int)
        right = defaultdict(int)
        
        for i, ele in enumerate(nums):
            if i % 2 == 0:
                left[ele] += 1
            else:
                right[ele] += 1
        
        rightSorted = []
        for key, value in right.items():
            rightSorted.append((value, key))
        
        rightSorted.sort()
        rightSortedLen = len(rightSorted)
        
        minOps = float('inf')
        halfLen = math.ceil(len(nums) / 2)
        for key, value in left.items():
            noOfOps = halfLen - value
            
            needEle = len(nums) - halfLen
            #print(needEle)
            if key in right:
                noOfOps += right[key]
                needEle -= right[key]
            
            if needEle > 0:
                
                #print(key, value)
                #print(rightSorted)
                if rightSorted[-1][1] == key:
                    noOfOps += (needEle - rightSorted[-2][0])
                else:
                    noOfOps += (needEle - rightSorted[-1][0])

            minOps = min(minOps, noOfOps)
        
        return minOps
                
        