class Solution:
    def numDecodings(self, s: str) -> int:
    # At each digit i, you have two choices:
        # Decode it as a single digit (1-9)
        # Decode it as a two digit number with the previous digit (10-26)

# dp[i] = number of ways to decode the first i characters
# dp[i] = dp[i-1] +dp[i-2]

        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty string has one way to decode
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) +1 ):

            dp[i] = 0
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]