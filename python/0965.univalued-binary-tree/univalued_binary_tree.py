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


def isUnivalTree(root):
        if not root:
            return True
        if root.right:
            if root.val != root.right.val:
                return False
        if root.left:
            if root.val != root.left.val:
                return False
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
