class Solution:
    def __init__(self):
        self.cost_tot = dict()

    def computeCost(self, cost, next_idx):
        if next_idx in self.cost_tot:
            return self.cost_tot[next_idx]

        if next_idx <= 2:
            self.cost_tot[next_idx] = cost[next_idx - 1]
            return cost[next_idx - 1]

        self.cost_tot[next_idx] = (
            min(
                self.computeCost(cost, next_idx - 1),
                self.computeCost(cost, next_idx - 2),
            )
            + cost[next_idx - 1]
        )
        return self.cost_tot[next_idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        cost.append(0)
        self.computeCost(cost, len(cost))
        return self.cost_tot[len(cost)]
