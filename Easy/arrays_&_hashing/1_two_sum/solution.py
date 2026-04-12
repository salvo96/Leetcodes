class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict = dict()

        for idx, num in enumerate(nums):
            lookup_dict[num] = idx

        for idx, num in enumerate(nums):
            value = lookup_dict.get(target - num)
            if value and value != idx:
                return [idx, value]
