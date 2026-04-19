class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        op_token = "+-*/"

        def operation(op1: int, op2: int, operand: str):
            if operand == "+":
                return op1 + op2
            if operand == "-":
                return op1 - op2
            if operand == "*":
                return op1 * op2
            if operand == "/":
                return int(op1 / op2)


        for token in tokens:
            if token in op_token:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operation(op1, op2, token))
            else:
                stack.append(int(token))

        return stack.pop()