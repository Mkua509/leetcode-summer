class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # Use flattening to combine all lists into one first
        combined_list = []
        for sublists in matrix:
            # Extend adds elements from an iterable to the end o current list
            combined_list.extend(sublists)
        
        # Now we use binary search on the flattened list
        left = 0
        right = len(combined_list) - 1
        while left <= right:
            mid = (left + right) // 2

            if combined_list[mid] == target:
                return True        
            elif combined_list[mid] <= target:
                left = mid + 1          
            else:
                right = mid - 1
        
        return False
