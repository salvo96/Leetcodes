class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        output_set = set()

        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ = nums[j] + nums[k] + nums[i]
                if sum_ == 0:
                    output_set.add((nums[i], nums[j], nums[k]))
                if sum_ > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return [list(triplet) for triplet in output_set]
