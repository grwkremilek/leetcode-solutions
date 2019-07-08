#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root):
    if not root: return 0
    return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

def maxDepth(root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
    
