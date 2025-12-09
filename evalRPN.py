class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stk.append(int(i))
            else:
                b = stk.pop()
                a = stk.pop()
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                elif i == '/':
                    res = int(a / b)
                stk.append(res)
        return stk[-1]