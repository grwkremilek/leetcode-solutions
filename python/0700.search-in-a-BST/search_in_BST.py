#https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def searchBST(root, val):
        if root is None or root.val == val: 
            return root
        if root.val < val: 
            return searchBST(root.right, val)
        return searchBST(root.left, val)


def searchBST(root, val):
    if root and root.val == val:
        return root
    if root and root.val > val:
        return searchBST(root.left, val)
    if root and root.val < val:
        return searchBST(root.right, val)
