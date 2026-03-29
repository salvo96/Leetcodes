class Solution:
    def __init__(
        self,
    ):
        self.output = dict()

    def compute_uniquePaths(self, row_idx, col_idx):
        if (row_idx, col_idx) in self.output:
            return self.output[(row_idx, col_idx)]

        if min(row_idx, col_idx) == 0:
            self.output[(row_idx, col_idx)] = 1
            return 1

        self.output[(row_idx, col_idx)] = self.compute_uniquePaths(
            row_idx - 1, col_idx
        ) + self.compute_uniquePaths(row_idx, col_idx - 1)
        return self.output[(row_idx, col_idx)]

    def uniquePaths(self, m: int, n: int) -> int:
        if min(m, n) == 1:
            return 1

        return self.compute_uniquePaths(m - 1, n - 1)
