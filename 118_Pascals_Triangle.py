class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1]]
        
        for i in range(1, numRows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, i):
                row[j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]
            
            pascalTriangle.append(row)
        
        return pascalTriangle
                
            
        