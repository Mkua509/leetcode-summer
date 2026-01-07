class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        value = self.stack[len(self.stack) - 1]

        # Apparently I could have just done self.stack[-1]
        return value
        

    def getMin(self):
        """
        :rtype: int
        """

        # I originally did minVal = 0 not good
        minVal = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < minVal:
                minVal = self.stack[i]
            else: 
                continue
        
        return minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()