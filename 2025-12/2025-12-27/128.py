class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # If not num essentiall means falsy in a boolean context: If 0, None, False or a empty collection such as list, string etc...
        if not nums:
            return 0
        result = 0
        nums.sort()

        current = nums[0]
        count = 0
        i = 0

        while i < len(nums):
            if current != nums[i]:
                current = nums[i]
                count = 0
            while i < len(nums) and current == nums[i]:
                i += 1
            count += 1
            current += 1
            result = max(result, count)
        return result