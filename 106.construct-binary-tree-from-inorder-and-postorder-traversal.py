#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # print(inorder)
        # print(postorder)
        val = postorder.pop()
        idx = inorder.index(val)
        
        right = self.buildTree(inorder[idx+1:],postorder)
        left = self.buildTree(inorder[:idx], postorder)
        root = TreeNode(val)
        
        root.left, root.right = left, right
        return root
# @lc code=end

