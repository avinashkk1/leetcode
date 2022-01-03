class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        st_map = {}
        t_set = set()
        for ch1, ch2 in zip(s, t):
            if ch1 in st_map:
                if st_map[ch1] != ch2:
                    return False
            else:
                if ch2 in t_set:
                    return False
                t_set.add(ch2)
                st_map[ch1] = ch2
        
        return True
                    