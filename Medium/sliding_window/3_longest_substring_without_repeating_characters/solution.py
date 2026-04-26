class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        max_length = 0

        left, right = 0, 0
        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1

            letters.add(s[right])
            max_length = max(max_length, len(letters))
            right += 1

        return max_length
