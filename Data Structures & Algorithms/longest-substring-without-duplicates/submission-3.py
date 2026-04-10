class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        longest = 0
        unique_chars = set()

        if len(s) < 2:
            return len(s)
        else:
            for end in range(len(s)):
                while s[end] in unique_chars:
                    unique_chars.remove(s[start])
                    start += 1
                unique_chars.add(s[end])

                longest = max(longest, end - start + 1)
                
            # unique_chars.add(s[start])
            # while end < len(s):
            #     while s[end] in unique_chars:
            #         unique_chars.remove(s[start])
            #         start += 1

            #     unique_chars.add(s[end])
            #     end += 1

            #     longest = max(longest, end - start)
            

            return longest

