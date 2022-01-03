class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        numSet = set()
        for i in range(9):
            numSet = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])
        
        for j in range(9):
            numSet = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])
        
        
        for p in range(0, 7, 3):
            for q in range(0, 7, 3):
                numSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[p + i][q + j] == ".":
                            continue
                        if board[p + i][q + j] in numSet:
                            return False
                        numSet.add(board[p + i][q + j])
    
        return True




