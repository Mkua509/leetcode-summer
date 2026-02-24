class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        HashPrev = {}

        for index, numbers in enumerate(nums):
            difference = target - numbers

            if difference in HashPrev:
                return [HashPrev[difference], index]
            
            HashPrev[nums[index]] = index