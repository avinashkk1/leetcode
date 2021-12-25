class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedHeights = [0] * 102
        for height in heights:
            expectedHeights[height] += 1
        
        nextHeight = count = 0
        for i in range(len(heights)):
            while expectedHeights[nextHeight] == 0:
                nextHeight += 1
            
            if nextHeight != heights[i]:
                count += 1
            
            expectedHeights[nextHeight] -= 1
        
        return count
        
        
        
    def heightChecker1(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        n = len(heights)
        count = 0
        for i in range(n):
            if expected[i] != heights[i]:
                count += 1
        
        return count
        