class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start, end = 0, 1
        longest = 0
        unique_count = set()

        if len(s) < 2:
            return len(s)
        else:
            unique_count.add(s[start])
            while end < len(s):
                while s[end] in unique_count:
                    unique_count.remove(s[start])
                    start += 1

                unique_count.add(s[end])
                end += 1

                longest = max(longest, end - start)
            

            return longest

