# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []

        if not root:
            return []
        
        queue = deque([root])
        while (len(queue)>0):
            queue_length = len(queue)
            children_values = []
            for _ in range(queue_length):
                node = queue.popleft()
                children_values.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            traversal.append(children_values)
        return traversal
        