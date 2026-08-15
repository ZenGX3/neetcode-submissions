class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [a-b for a, b in zip(gas, cost)]
        t = 0
        s = 0
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            t += diff[i]
            if t < 0:
                t = 0
                s = i + 1
        return s
                
