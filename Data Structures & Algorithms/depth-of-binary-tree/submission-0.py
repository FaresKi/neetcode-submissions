# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs (node: Optional[TreeNode], depth) -> int:
            print(f"depth: {depth}")
            if node is None:
                pass
            for child in [node.left, node.right]:
                if child is not None:
                    depth+=1
                    dfs(child, depth)
            
            return depth

        if root is None:
            return 0
        return dfs(root, 1)
        

