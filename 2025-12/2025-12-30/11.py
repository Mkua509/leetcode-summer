class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right =  len(height) - 1
        largest_area = 0


        while left < right:
            temp_height = min(height[left], height[right])
            temp = (right - left) * temp_height

            if temp > largest_area:
                largest_area = temp

            if height[left] >= height[right]:
                right -= 1
            else: 
                left += 1 


        return largest_area     