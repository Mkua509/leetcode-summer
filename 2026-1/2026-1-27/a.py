# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                # Is balanced and height = 0
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # Here we must consider that dfs returns boolean left[0]/right[0] requires that the tree is already balanced as one of its requirements 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        # Remeber that dfs returns a list value, in this case we will return if the value is balanced (True, False)
        return dfs(root)[0]