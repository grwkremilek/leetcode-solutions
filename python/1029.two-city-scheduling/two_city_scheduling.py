#https://leetcode.com/problems/two-city-scheduling/

def twoCitySchedCost(costs):
    costs = sorted(costs, key=lambda cost: cost[0]-cost[1])
    return sum(cost[0] for cost in costs[:len(costs)//2]) + sum(cost[1] for cost in costs[len(costs)//2:])
