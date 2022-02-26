class Bitset:

    def __init__(self, size: int):
        self.myBitSet = [0] * size
        self.isFlipped = False
        self.noOfOnes = 0
        self.noOfZeroes = size
        

    def fix(self, idx: int) -> None:
        if self.isFlipped:
            if self.myBitSet[idx] == 1:
                self.myBitSet[idx] = 0
                self.noOfOnes += 1   
                self.noOfZeroes -= 1
        else:
            if self.myBitSet[idx] == 0:
                self.myBitSet[idx] = 1
                self.noOfOnes += 1
                self.noOfZeroes -= 1
        #print(self.noOfZeroes)
        
    def unfix(self, idx: int) -> None:
        if self.isFlipped:
            if self.myBitSet[idx] == 0:
                self.myBitSet[idx] = 1
                self.noOfZeroes += 1
                self.noOfOnes -= 1
        else:
            if self.myBitSet[idx] == 1:
                self.myBitSet[idx] = 0
                self.noOfOnes -= 1
                self.noOfZeroes += 1

        

    def flip(self) -> None:
        if self.isFlipped:
            self.isFlipped = False
                  
        else:
            self.isFlipped = True
        
        self.noOfOnes, self.noOfZeroes = self.noOfZeroes, self.noOfOnes   
        

    def all(self) -> bool:
        
        if self.noOfZeroes > 0:
            return False
        return True
        

    def one(self) -> bool:
        if self.noOfOnes > 0:
            return True
        return False
        

    def count(self) -> int:
        return self.noOfOnes
        

    def toString(self) -> str:
        if self.isFlipped:
            return ''.join([str(1 - ele) for ele in self.myBitSet])
        return ''.join([str(ele) for ele in self.myBitSet])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()