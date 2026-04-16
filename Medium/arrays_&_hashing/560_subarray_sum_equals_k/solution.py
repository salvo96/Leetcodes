class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output_counter = 0

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        prefix_count = {0: 1}

        # increase counter: current_prefix - previous_prefix == k   ---> previous_prefix == current_prefix - k
        for num in prefix:
            output_counter += prefix_count.get(num - k, 0)
            prefix_count[num] = prefix_count.get(num, 0) + 1

        return output_counter
