# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        count = [k]
        result = [0]

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)
            count[0] -= 1

            if count[0] == 0:
                result[0] = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return result[0]