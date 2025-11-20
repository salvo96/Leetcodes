class Solution:
    def backtrack(self, candidates, start, candidate, solution, target):
        if sum(candidate) == target:
            solution.append(candidate.copy())
        elif sum(candidate) < target:
            for i in range(start, len(candidates)):
                num = candidates[i]
                candidate.append(num)
                self.backtrack(candidates, i, candidate, solution, target)
                candidate.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        self.backtrack(candidates, 0, [], solution, target)
        return solution
