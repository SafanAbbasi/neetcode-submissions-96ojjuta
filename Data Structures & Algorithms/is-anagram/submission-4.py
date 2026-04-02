from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)

        # other option
        # if len(s) != len(t): 
        #     return False

        # schardict = defaultdict(int)
        # tchardict = defaultdict(int)

        # for char in s:
        #     schardict[char] += 1
        
        # for char in t:
        #     tchardict[char] += 1
        
        # if schardict == tchardict:
        #     return True
        
        # return False


        ### Unique approch using fixed 26 length array = Hash Table
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26
        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False
        # return True

