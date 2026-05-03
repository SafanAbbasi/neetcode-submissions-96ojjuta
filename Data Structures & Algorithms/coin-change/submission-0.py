class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unlimited options per coin

        # what's the minimum number of coins to make amount i?
        # dp[i] = min(dp[i - c] + 1) for all coins c


        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount+1): 
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i],dp[i-c] + 1)


        
        return -1 if dp[amount] == float('inf') else dp[amount]