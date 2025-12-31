class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Checks if there is an exisiting value in list first
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        result = 0

        while left < right: 
            if maxleft < maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                result += maxleft - height[left]
            else: 
                right -= 1
                maxright = max(maxright, height[right])
                result += maxright - height[right]

        return result