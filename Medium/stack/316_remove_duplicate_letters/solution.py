class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        duplicates = dict()
        stack = list()

        for letter in s:
            if duplicates.get(letter):
                duplicates[letter] += 1
            else:
                duplicates[letter] = 1

        for letter in s:
            duplicates[letter] -= 1

            if letter in stack:
                continue

            while len(stack) > 0 and stack[-1] > letter and duplicates[stack[-1]] > 0:
                stack.pop()

            stack.append(letter)

        return "".join(stack)
