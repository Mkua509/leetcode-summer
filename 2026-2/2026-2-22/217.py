class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        set_nums = set()

        for numbers in nums:
            if numbers in set_nums:
                return True
            else:
                set_nums.add(numbers)
        
        return False