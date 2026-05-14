class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_subsets = []

        def explore_solution(solution: list, start_idx: int):
            nonlocal nums_subsets

            nums_subsets.append(solution.copy())

            for idx in range(start_idx, len(nums)):
                solution.append(nums[idx])

                explore_solution(solution, idx + 1)

                solution.pop()

        explore_solution([], 0)

        return nums_subsets
