import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_nums = []

        for num in nums:
            heapq.heappush(largest_nums, num)

            if len(largest_nums) > k:
                heapq.heappop(largest_nums)

        return largest_nums[0]

        