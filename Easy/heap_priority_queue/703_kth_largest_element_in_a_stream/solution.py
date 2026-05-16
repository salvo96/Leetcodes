import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.test_scores = nums

        heapq.heapify(self.test_scores)

        while len(self.test_scores) > k:
            heapq.heappop(self.test_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.test_scores, val)

        if len(self.test_scores) > self.k:
            heapq.heappop(self.test_scores)

        return self.test_scores[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
