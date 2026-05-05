# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        res = -1

        def inorder(node):
            nonlocal res
            nonlocal count
            
            if not node or res != -1: 
                return
            

            inorder(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res