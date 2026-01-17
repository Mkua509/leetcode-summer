class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = 0
        while n:
            n &= (n-1)
            counts += 1
        return counts