# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
            
        a=inorder(root1)
        b=inorder(root2)
        a.extend(b)
        a.sort()
        return a