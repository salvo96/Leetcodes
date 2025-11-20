from math import sqrt
import heapq


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        distance_self = sqrt((self.x) ** 2 + (self.y) ** 2)
        distance_other = sqrt((other.x) ** 2 + (other.y) ** 2)

        return distance_self > distance_other


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = []
        for point in points:  # O(n)
            heapq.heappush(heap_list, Point(point[0], point[1]))  # O(log(k))

            if len(heap_list) > k:
                heapq.heappop(heap_list)  # O(log(k))

        output_list = []
        for _ in range(k):  # O(k)
            point = heapq.heappop(heap_list)  # O(log(k))
            output_list.append([point.x, point.y])
        output_list.reverse()
        return output_list
