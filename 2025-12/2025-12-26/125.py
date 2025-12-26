class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_string = ""
        
        for c in s:
        
        # c.isalnum essentially checks if a character is alpha numeric or not, by labelling as False or True it'll only pass the if statment if it is True. The true value will be added to the new string aftre getting lowered.
            if c.isalnum():

                # += adds to the list which I dind't remember
                new_string += c.lower()
        
        s = new_string

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True