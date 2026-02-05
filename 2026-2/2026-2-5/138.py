"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = { None : None}

        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next
        
        current = head
        while current: 
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next
        
        return oldToCopy[head]