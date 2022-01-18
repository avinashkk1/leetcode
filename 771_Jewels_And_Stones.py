class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()
        for ch in jewels:
            jewelSet.add(ch)
        
        count = 0
        for ch in stones:
            if ch in jewelSet:
                count += 1
        
        return count
        