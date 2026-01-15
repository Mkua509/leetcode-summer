# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # Fast and slow approach but first split the list in half

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        second_half = slow.next
        # We need to disconnect the previous half
        prev = slow.next = None

        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        

