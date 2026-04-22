class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif (
                nums[left] <= nums[middle]
            ):  # the left side is monotonic: the right side might be not monotonic
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:  # the left side is not monotonic: the right side for sure is monotonic
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
