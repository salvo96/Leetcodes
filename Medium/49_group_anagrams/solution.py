class Solution:
    def count_string(self, str_):
        letters_count = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
        for letter in str_:
            letters_count[letter] += 1
        return str([val for val in letters_count.values()])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_anagrams = {}
        for str_ in strs:  #   O(N)
            key = self.count_string(str_)  # O(k)
            if unique_anagrams.get(key):
                unique_anagrams[key].append(str_)
            else:
                unique_anagrams[key] = [str_]

        return list(unique_anagrams.values())
