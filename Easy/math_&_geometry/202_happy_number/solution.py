class Solution:
    def isHappy(self, n: int) -> bool:
        def compute_num(n: int):
            str_n = str(n)
            res = 0
            for digit in str_n:
                res += int(digit) ** 2
            return res

        visited_nums = set()
        while n != 1:
            n = compute_num(n)
            if n in visited_nums:
                return False
            visited_nums.add(n)
        return True
