class Solution:
    def isPalindrome(self, s: str) -> bool:

        # return s.lower() == s[::-1].lower()
        cleaned = "".join(c for c in s.lower() if c.isalnum())
        return cleaned == cleaned[::-1]

        # left , right = 0, len(s) - 1
        # while left < right:
        #     if s[left].isalnum():

