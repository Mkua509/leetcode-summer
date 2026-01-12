# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head

        while curr:

            # Temp value is now the next value in list
            temp = curr.next
            # reverse the current values pointer
            curr.next = prev
            # Move previous value forward one 
            prev = curr
            # Move current value forward one
            curr = temp
        
        return prev

