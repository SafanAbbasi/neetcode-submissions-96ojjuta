from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # don't care about order. just freq
        # don't want to use 26 length array since there are also capital letters
        # dynamic window size
        # when to move and increment.
        # Don't try to find a "first letter" — just add every character to the window unconditionally.
        freq_t = Counter(t)

        freq_s = defaultdict(int)
        start = 0 
        unique_char = 0
        shortest = float('inf')
        res = ""

        for end in range(len(s)):
            
            freq_s[s[end]] += 1
            
            if freq_s[s[end]] == freq_t[s[end]]:
                unique_char += 1
            
            while unique_char == len(freq_t):

                # save shortest
                if end - start + 1 < shortest:
                    shortest = end - start + 1
                    res = s[start:end + 1]

                # shrink
                freq_s[s[start]] -= 1
                if freq_s[s[start]] < freq_t[s[start]]:
                    unique_char -= 1
                start += 1


        return res