class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # i = floor of the staircase
        # two options again of one step ahead or two steps ahead

        # trying to reach len[cost] + 1 

        # dp[i] = minimum cost to reach step i
        # dp[0] = ?  # cost to reach step 0
        # dp[1] = ?  # cost to reach step 1

        dp = collections.defaultdict(int)
        dp[0] = 0
        dp[1] = 0
        # dp[2] = min( (dp[0] + cost[0]) , (dp[1]+cost[1]))

        for i in range(2, len(cost)+1):

           dp[i] = min( (dp[i-1] + cost[i-1]) , (dp[i-2]+cost[i-2]))

        return dp[len(cost)]