class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        output = list()

        counter = m * n

        min_row, max_row, min_col, max_col = 0, m - 1, 0, n - 1

        while counter > 0:
            row, col = min_row, min_col
            # 1. Right -> (k row, i+ column)
            while col <= max_col and counter > 0:
                output.append(matrix[row][col])
                counter -= 1
                col += 1
            min_row += 1
            row, col = min_row, col - 1

            # 2. Down -> (i+ row, k column)
            while row <= max_row and counter > 0:
                output.append(matrix[row][col])
                counter -= 1
                row += 1
            max_col -= 1
            row, col = row - 1, max_col

            # 3. Left -> (k row, i- column)
            while col >= min_col and counter > 0:
                output.append(matrix[row][col])
                counter -= 1
                col -= 1
            max_row -= 1
            row, col = max_row, col + 1

            # 4. Up -> (i- row, k column)
            while row >= min_row and counter > 0:
                output.append(matrix[row][col])
                counter -= 1
                row -= 1
            min_col += 1
        return output
