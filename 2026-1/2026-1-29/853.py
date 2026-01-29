class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        stack_result = []
        for p, s in sorted(pair)[::-1]: # Reverse the sorted order
            stack_result.append(float(target - p) / s)
            if len(stack_result) >= 2 and stack_result[-1] <= stack_result[-2]:
                stack_result.pop()
        

        return len(stack_result)