class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length_nums = len(nums)
        
        # Create a list of 1s in a length of numbers
        result = [1] * length_nums

        # left side of pivot value
        left = 1
        for i in range(length_nums):
            result[i] = left
            left = left * nums[i]
        
        # Right side of pivot values
        right = 1
        # range(start, stop, step)
        for i in range(length_nums - 1, -1 , -1):
            result[i] = result[i] * right
            right = right * nums[i]
        
        return result