from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # allow for up to k replacements
        # what to do at the value thats not the same and k? then decrement k value and keep going if its not 0
        # if k is 0 then remove left character until we remove a diff char than the main one. 


        start = 0
        longest = 0
        freq = defaultdict(int)
        maxFreq = 0


        for end in range(len(s)):
            freq[s[end]] += 1
            maxFreq = max(maxFreq, freq[s[end]])

            window_length = end - start + 1

            if window_length - maxFreq > k:
                freq[s[start]] -= 1
                start += 1

            
                        
            longest = max(longest, end - start + 1)

        
        return longest