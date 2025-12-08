class Solution:
    def dfs(self, row, col, grid):
        grid[row][col] = "-1"

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for direction in directions:
            row_idx = row + direction[0]
            col_idx = col + direction[1]
            if (0 <= row_idx < len(grid)) & (0 <= col_idx < len(grid[0])):
                if grid[row_idx][col_idx] == "1":
                    self.dfs(row_idx, col_idx, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for row_idx, _ in enumerate(grid):
            for col_idx, _ in enumerate(grid[0]):
                if grid[row_idx][col_idx] == "1":
                    self.dfs(row_idx, col_idx, grid)
                    counter += 1
        return counter
