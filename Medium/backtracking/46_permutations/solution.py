class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def process_solution(solution: List[int], used: set):
            nonlocal permutations

            if len(solution) == len(nums):
                permutations.append(solution.copy())
                return

            for idx in range(len(nums)):
                num = nums[idx]

                if num not in used:
                    solution.append(num)
                    used.add(num)

                    process_solution(solution, used)

                    solution.pop()
                    used.remove(num)

        process_solution([], set())

        return permutations
