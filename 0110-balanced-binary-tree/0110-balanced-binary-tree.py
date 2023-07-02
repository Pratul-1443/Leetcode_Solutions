# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root==None:
                return 0
            return 1+max(height(root.left),height(root.right))
        
        if root==None:
            return True
        leftpart=height(root.left)
        rightpart=height(root.right)
        
        if (leftpart-rightpart)>1 or (rightpart - leftpart) >1:
            return False
        l=self.isBalanced(root.left)
        r=self.isBalanced(root.right)
        if l and r:
            return True
        else:
            return False
        
        
   