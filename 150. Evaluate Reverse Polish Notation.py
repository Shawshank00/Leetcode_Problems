class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:

            if i == '+':
                pop1 = stk.pop()
                pop2 = stk.pop()
                stk.append(pop2 + pop1)
            
            elif i == '-':
                pop1 = stk.pop()
                pop2 = stk.pop()
                stk.append(pop2 - pop1)
            
            elif i == '*':
                pop1 = stk.pop()
                pop2 = stk.pop()
                stk.append(pop2 * pop1)
            
            elif i == '/':
                pop1 = stk.pop()
                pop2 = stk.pop()
                stk.append(int(pop2 / pop1))
            
            else:
                stk.append(int(i))
            
        return stk[-1]
