class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if root is None:
            return 0
        
        leftTree = self.maxDepth(root.left)
        rightTree = self.maxDepth(root.right)
        value = max(leftTree, rightTree) + 1

        return value