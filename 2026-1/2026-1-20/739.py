class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        output = [0] * len(temperatures)
        stack = [] # Two pars [temp, index]

        for index, temp in enumerate(temperatures):
            # stack[-1][0] finds the first element [0] in the last item [-1] so its a list in a list 
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return output