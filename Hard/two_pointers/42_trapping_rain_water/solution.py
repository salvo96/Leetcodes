class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        output = 0

        while left <= right:
            if max_left <= max_right:
                output += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                output += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        return output
