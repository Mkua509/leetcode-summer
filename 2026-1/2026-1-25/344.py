class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        length_string = len(s)
        left = 0 
        right = len(s) - 1

        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]
            
            # Move pointers inward
            left += 1
            right -= 1
        
        # Join the list back into a string
        return "".join(s)

