class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_no_duplicates(row_start, row_end, col_start, col_end, by_row=True):
            for i in range(row_start, row_end):
                seen = set()
                count = 0

                for j in range(col_start, col_end):
                    value = board[i][j] if by_row else board[j][i]

                    if value != ".":
                        seen.add(value)
                        count += 1

                if len(seen) < count:
                    return False

            return True

        def box_has_no_duplicates(row_start, row_end, col_start, col_end):
            seen = set()
            count = 0

            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    value = board[i][j]

                    if value != ".":
                        seen.add(value)
                        count += 1

            return len(seen) == count

        if not has_no_duplicates(0, 9, 0, 9, by_row=True):
            return False

        if not has_no_duplicates(0, 9, 0, 9, by_row=False):
            return False

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                if not box_has_no_duplicates(
                    row_start, row_start + 3, col_start, col_start + 3
                ):
                    return False

        return True
