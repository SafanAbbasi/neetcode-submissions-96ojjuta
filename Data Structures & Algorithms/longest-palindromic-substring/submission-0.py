class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l + 1, r 

        for i in range(len(s)):
            
            l, r = expand(i, i)
            if r - l > resLen:
                resLen = r - l
                res = s[l:r]
            l, r = expand(i,i+1)
            if r - l > resLen:
                resLen = r - l
                res = s[l:r]

        return res