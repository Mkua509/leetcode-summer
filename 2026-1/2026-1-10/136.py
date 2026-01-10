class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0 # n ^ 0 = n
        for numbers in nums:
            result = numbers ^ result
        return result