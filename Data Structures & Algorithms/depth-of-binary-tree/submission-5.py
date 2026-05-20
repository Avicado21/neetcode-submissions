from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def maxDepth(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])

        count = 0

        if(queue == deque([None])):
            return 0

        while queue:
            count+=1

            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if(node.left != None):
                    queue.append(node.left)

                if(node.right != None):
                    queue.append(node.right)

        return count




        

        

        