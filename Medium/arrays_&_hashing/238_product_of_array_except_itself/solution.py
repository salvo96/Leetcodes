class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = len(nums) * [1], len(nums) * [1]

        for i in range(len(nums) - 1):
            prefix[i + 1] = prefix[i] * nums[i]

        for i in range(-1, -len(nums), -1):
            postfix[i - 1] = postfix[i] * nums[i]

        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i] * postfix[i])

        return answer
