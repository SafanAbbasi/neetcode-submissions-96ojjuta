class Solution:
    def isPalindrome(self, s: str) -> bool:

        # cleaned = "".join(c for c in s.lower() if c.isalnum())
        # return cleaned == cleaned[::-1]

        left , right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left +=1
                right -= 1
        
            if not s[left].isalnum() and s[right].isalnum():
                left += 1
            if s[left].isalnum() and not s[right].isalnum():
                right -= 1
            if not s[left].isalnum() and not s[right].isalnum():
                left += 1
                right -= 1
        
        return True