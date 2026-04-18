class Solution:
    def isValid(self, s: str) -> bool:
        def get_closed_parenthesis(open_p: str):
            if open_p == "(":
                return ")"
            if open_p == "[":
                return "]"
            if open_p == "{":
                return "}"
            return None

        stack = list()

        for p in s:
            closed_p = get_closed_parenthesis(p)
            if closed_p:
                stack.append(closed_p)
            else:
                if not stack:
                    return False
                if stack.pop() != p:
                    return False
        return len(stack) == 0
