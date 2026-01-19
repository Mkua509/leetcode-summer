class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        result = 0
        
        while left <= right:
            # Current value is basically mid
            current_speed = (right + left) // 2
            total_time = 0
            for pile in piles:
                # Need to force float division
                total_time = total_time + (math.ceil(float(pile) / current_speed))
            if total_time <= h:
                result = current_speed
                right = current_speed - 1
            else: 
                left = current_speed + 1
        
        return result