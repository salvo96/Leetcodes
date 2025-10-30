class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        days = len(temperatures) * [0]

        for idx, temperature in enumerate(temperatures):
            while len(stack) > 0:
                if temperature > temperatures[stack[-1]]:
                    idx_to_change = stack.pop()
                    days[idx_to_change] = idx - idx_to_change
                else:
                    break
            stack.append(idx)
        return days
