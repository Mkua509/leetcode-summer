class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        result = 0
        charSet = set(s)

        for character in charSet:
            # Count being the count of characters inside sliding window
            count = left = 0

            for right in range(len(s)):
                if s[right] == character:
                    count += 1
                
                while (right - left + 1) - count > k:
                    if s[left] == character:
                        count -= 1
                    left += 1
                result = max(result, right - left + 1)
        
        return result