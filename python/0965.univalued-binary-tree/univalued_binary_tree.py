#https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isUnivalTree(root):
    def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res += inorderTraversal(root.right)
        return res
    return len(set(inorderTraversal(root))) == 1
