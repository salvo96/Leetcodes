class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        min_idx = 0
        max_idx = len(height) - 1

        while min_idx < max_idx:
            area = min(height[min_idx], height[max_idx]) * (max_idx - min_idx)
            if area > max_area:
                max_area = area

            if height[min_idx] < height[max_idx]:
                min_idx += 1
            else:
                max_idx -= 1

        return max_area
