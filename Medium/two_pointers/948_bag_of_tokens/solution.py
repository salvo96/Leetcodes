class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        min_idx = 0
        max_idx = len(tokens) - 1
        score = 0

        tokens.sort()

        while min_idx <= max_idx:
            if power >= tokens[min_idx]:
                score += 1
                power -= tokens[min_idx]
                min_idx += 1
            else:
                if score == 0 or min_idx == max_idx:
                    break
                else:
                    score -= 1
                    power += tokens[max_idx]
                    max_idx -= 1
        return score
