from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])

        if not root:
            return []

        big = []

        while queue:
            size = len(queue)

            small = []

            for i in range(size):
                node = queue.popleft()

                small.append(node.val)

                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)

            big.append(small)
        
        return big

        

        
    



        