class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            False

        reverse = 0
        temp_x = x
        
        while x > 0:
            reverse = (reverse * 10) + (x%10)
            x //= 10

        return reverse == temp_x