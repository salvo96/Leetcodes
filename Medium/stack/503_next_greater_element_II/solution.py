class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = n * [0]

        stack = []
        for i in range(2 * n - 1, -1, -1):
            idx = i % n

            while stack and stack[-1] <= nums[idx]:
                stack.pop()

            if i < n:
                if stack and stack[-1] > nums[idx]:
                    output[idx] = stack[-1]
                else:
                    output[idx] = -1

            stack.append(nums[idx])
        return output
