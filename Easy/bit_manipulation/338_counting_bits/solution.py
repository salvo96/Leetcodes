class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = (n + 1) * [0]

        for i in range(1, n + 1):
            ans[i] = (i & 1) + ans[i >> 1]

        return ans
