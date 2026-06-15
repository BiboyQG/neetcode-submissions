class Solution:
    def calPoints(self, operations: List[str]) -> int:

        def is_number(el):
            try:
                float(el)
                return True
            except ValueError:
                return False

        stack = []

        for i in range(len(operations)):
            if not is_number(operations[i]):
                if operations[i] == "+":
                    stack.append(stack[-1] + stack[-2])
                if operations[i] == "D":
                    stack.append(2 * stack[-1])
                if operations[i] == "C":
                    stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)
            