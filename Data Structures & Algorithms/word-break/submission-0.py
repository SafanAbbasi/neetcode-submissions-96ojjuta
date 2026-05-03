class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # split s using only dictionary words. Need perfect split with no remaining chars in s 

        dp = [False] * (len(s)  +1)

        dp[0] = True # empty string will always be true

        for idx in range(1, len(s)+1):
            for j in range(idx):
                if dp[j] and s[j:idx] in wordDict:
                    dp[idx] = True
                    break

        return dp[len(s)]