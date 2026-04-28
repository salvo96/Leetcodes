class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = dict()
        s2_letters = dict()

        for c in s1:
            s1_letters[c] = s1_letters.get(c, 0) + 1

        left, right = 0, 0
        while right < len(s2):
            s2_letters[s2[right]] = s2_letters.get(s2[right], 0) + 1

            if not right - left + 1 < len(s1):
                count_eq = 0
                for key in s1_letters:
                    if s1_letters[key] != s2_letters.get(key, 0):
                        break
                    count_eq += 1
                if count_eq == len(s1_letters):
                    return True

                s2_letters[s2[left]] -= 1
                left += 1

            right += 1

        return False
