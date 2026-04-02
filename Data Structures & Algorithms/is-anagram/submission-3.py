from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)

        # other option
        # schardict = defaultdict(int)
        # tchardict = defaultdict(int)

        # for char in s:
        #     schardict[char] += 1
        
        # for char in t:
        #     tchardict[char] += 1
        
        # if schardict == tchardict:
        #     return True
        
        # return False

