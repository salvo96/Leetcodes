class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Determine if zeros are in the first row and col
        first_row_flag = False
        first_col_flag = False
        for col in range(n):
            if matrix[0][col] == 0:
                first_row_flag = True
        for row in range(m):
            if matrix[row][0] == 0:
                first_col_flag = True

        # Set to first element of col/row to zero when a zero in submatrix is met
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # Use the first zero of col/row to set to zero the entire row/col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # Set first col/row to zero when the flags are True
        if first_row_flag:
            for col in range(n):
                matrix[0][col] = 0
        if first_col_flag:
            for row in range(m):
                matrix[row][0] = 0
