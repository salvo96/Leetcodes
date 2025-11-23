class Solution:
    def check_candidate(self, candidate):
        check_counter = 0
        for sym in candidate:
            if sym == "(":
                check_counter += 1
            else:
                check_counter -= 1
                if check_counter < 0:
                    return False
        return check_counter == 0

    def backtrack(self, n, candidate, solution, open_cnt=0, close_cnt=0):
        if open_cnt > n or close_cnt > open_cnt:
            return

        if len(candidate) == 2 * n:
            if self.check_candidate(candidate):
                solution.add("".join(candidate))
            return

        candidate.append("(")
        self.backtrack(n, candidate, solution, open_cnt + 1, close_cnt)
        candidate.pop()

        candidate.append(")")
        self.backtrack(n, candidate, solution, open_cnt, close_cnt + 1)
        candidate.pop()
