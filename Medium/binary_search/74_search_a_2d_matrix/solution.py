class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_row = 0
        j_row = len(matrix) - 1

        while i_row <= j_row:
            pointer_row = int((i_row + j_row) / 2)
            if (
                matrix[pointer_row][0]
                <= target
                <= matrix[pointer_row][len(matrix[pointer_row]) - 1]
            ):
                break
            elif target < matrix[pointer_row][0]:
                j_row = pointer_row - 1
            else:
                i_row = pointer_row + 1

        i_col = 0
        j_col = len(matrix[pointer_row]) - 1

        while i_col <= j_col:
            pointer_col = int((i_col + j_col) / 2)
            if target < matrix[pointer_row][pointer_col]:
                j_col = pointer_col - 1
            elif target > matrix[pointer_row][pointer_col]:
                i_col = pointer_col + 1
            else:
                return True

        return False
