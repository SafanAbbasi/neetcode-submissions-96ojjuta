class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # need to track amount and also num of combinations?
        memo = {}

        # dp[0][0]

        # base case if total is greater than to amount then return 0
        # base case if i >= len(coins), return 0

        # So your two state variables are:

        # i — which coin you're currently deciding on
        # total — how much you've accumulated so far

        # And your two choices at each step are:

        # Use coin i (stay on same coin since you have unlimited) → total + coins[i]
        # Skip coin i → move to next coin i+1, total stays same


        def dfs(i, total):
            
            if i >= len(coins):
                return 0
            if total > amount:
                return 0       

            if (i,total) in memo:
                return memo[(i,total)]

            if total == amount:
                return 1
            # stay on same coin
            staycount = dfs(i,total+coins[i])

            # move onto next coin
            skipcount = dfs(i+1, total)

            memo[(i,total)] = (staycount + skipcount)

            return memo[(i,total)]
            # return staycount + skipcount


        return dfs(0,0) # inital state

