class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curfuel = 0 
        start = 0 

        for station, fuel in enumerate(gas):
            curfuel += fuel 

            if curfuel - cost[station] < 0:
                curfuel = 0 
                start = station +1
            else:
                curfuel -= cost[station]

        return start if sum(gas) >= sum(cost) else -1