class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_subs_len = 0
        letters_freq = {c: 0 for c in s}
        max_freq = 0

        left, right = 0, 0
        while right < len(s):
            letters_freq[s[right]] += 1
            subs_len = right - left + 1
            max_freq = max(max_freq, letters_freq[s[right]])

            while subs_len - max_freq > k:
                letters_freq[s[left]] -= 1
                left += 1
                subs_len = right - left + 1

            max_subs_len = max(max_subs_len, subs_len)
            right += 1
        return max_subs_len
