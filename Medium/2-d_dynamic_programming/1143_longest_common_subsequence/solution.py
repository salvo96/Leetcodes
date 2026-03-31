class Solution:
    def __init__(
        self,
    ):
        self.output = dict()

    def compute_longestCommonSubsequence(self, text1, text2, m, n):
        if (m, n) in self.output:
            return self.output[(m, n)]

        if text1[m] == text2[n]:
            equal_val = 1
        else:
            equal_val = 0

        if m == 0 and n == 0:
            self.output[(m, n)] = equal_val
            return self.output[(m, n)]

        if m == 0:
            self.output[(m, n)] = max(
                self.compute_longestCommonSubsequence(text1, text2, 0, n - 1), equal_val
            )
            return self.output[(m, n)]
        if n == 0:
            self.output[(m, n)] = max(
                self.compute_longestCommonSubsequence(text1, text2, m - 1, 0), equal_val
            )
            return self.output[(m, n)]

        if equal_val == 1:
            self.output[(m, n)] = (
                self.compute_longestCommonSubsequence(text1, text2, m - 1, n - 1)
                + equal_val
            )
        else:
            self.output[(m, n)] = max(
                self.compute_longestCommonSubsequence(text1, text2, m, n - 1),
                self.compute_longestCommonSubsequence(text1, text2, m - 1, n),
            )
        return self.output[(m, n)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1:
            return 1 if text1 in text2 else 0
        if len(text2) == 1:
            return 1 if text2 in text1 else 0

        return self.compute_longestCommonSubsequence(
            text1, text2, len(text1) - 1, len(text2) - 1
        )
