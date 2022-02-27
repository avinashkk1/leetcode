class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for string in words:
            if string.startswith(pref):
                count += 1
        
        return count
        