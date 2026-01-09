class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for current in tokens:
            if current == '+':
                stack.append(stack.pop() + stack.pop())
            elif current == '*':
                stack.append(stack.pop() * stack.pop())
            elif current == '/':
                a = stack.pop()
                b = stack.pop()

                stack.append(int(float(b) / a))
            elif current == '-':
                a = stack.pop() 
                b = stack.pop() 
                stack.append(b - a)
            else:
                stack.append(int(current))
                
        return stack[0]     