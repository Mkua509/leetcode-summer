class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
        
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threesum = a + nums[left] + nums[right]

                if threesum > 0:
                    right = right - 1

                elif threesum < 0:
                    left = left + 1
                else: 
                    results.append([a, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while nums[left] == nums[left - 1] and left < right:
                        left = left + 1
        return results