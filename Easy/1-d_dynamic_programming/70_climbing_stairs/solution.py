class Solution:
    def __init__(
        self,
    ):
        self.memo = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.memo.get(n):
            return self.memo[n]

        n_ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = n_ways

        return n_ways
