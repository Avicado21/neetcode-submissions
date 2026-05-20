# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #as with all dfs:
        if not root:
            return

        
        # need concurrent swapping so
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)

        return root

        