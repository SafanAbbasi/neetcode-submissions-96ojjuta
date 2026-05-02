class Solution:
    def climbStairs(self, n: int) -> int:
        # given steps
        # two choices each time

        # n =1 
        # f(0) = 1 doesn't mean "1 way to take steps to reach 0". 
        # It means "there is 1 valid way to exist at the starting position" — which is just... standing there doing nothing.
        
        one = 1 # f(0)
        two = 1 # f(1)
        total = 0
        if n < 2:
            return 1
        for i in range(2,n+1):
            
            total = (one + two)
            one = two
            two = total

        return total

