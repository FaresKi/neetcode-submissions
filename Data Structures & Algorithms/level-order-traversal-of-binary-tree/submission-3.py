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
        level = 0
        while len(queue) > 0:
            children_vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    break
                children_vals.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        
            traversal.append(children_vals)
        return traversal
