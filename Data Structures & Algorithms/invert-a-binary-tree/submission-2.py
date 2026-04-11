# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        if cur == None:
            return
        
        temp = cur.left
        cur.left = cur.right
        cur.right = temp
        self.invertTree(cur.right)
        self.invertTree(cur.left)
        return root
        

