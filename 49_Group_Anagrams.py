class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for strIndex, string in enumerate(strs):
            charFreq = [0] * 26
            for ch in string:
                charFreq[ord(ch) - ord('a')] += 1
            s = ''
            for i in range(97, 123):
                s += chr(i) + str(charFreq[i - 97])
            if s in anagramDict:
                anagramDict[s].append(strIndex)
            else:
                anagramDict[s] = [strIndex]
        
        ans = []
        for anagram, indices in anagramDict.items():
            items = []
            for item in indices:
                items.append(strs[item])
            ans.append(items)
        
        return ans
            
            
        