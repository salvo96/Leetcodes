class Solution:
    def __init__(
        self,
    ):
        self.output = dict()

    def compute_rob(self, nums, n):
        if n in self.output:
            return self.output[n]

        if n <= 2:  #   Base Cases
            self.output[n] = max(nums[:n])
            return self.output[n]

        self.output[n] = max(
            self.compute_rob(nums, n - 1), self.compute_rob(nums, n - 2) + nums[n - 1]
        )
        return self.output[n]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return self.compute_rob(nums, len(nums))
