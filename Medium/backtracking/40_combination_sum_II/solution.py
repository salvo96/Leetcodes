class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        candidates.sort()

        def process_candidate(candidate: List[int], start_idx: int, candidate_sum: int):
            nonlocal combinations

            if candidate_sum == target:
                combinations.append(candidate.copy())

            if candidate_sum >= target:
                return

            for idx in range(start_idx, len(candidates)):
                if idx > start_idx and candidates[idx - 1] == candidates[idx]:
                    continue

                num = candidates[idx]

                candidate_sum += num
                candidate.append(num)

                process_candidate(candidate, idx + 1, candidate_sum)

                candidate.pop()
                candidate_sum -= num

        process_candidate([], 0, 0)

        return combinations
