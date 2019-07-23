#https://leetcode.com/problems/merge-two-binary-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def mergeTrees(t1, t2):
    if t1 or t2:
        root = TreeNode((t1 and t1.val or 0) + (t2 and t2.val or 0))
        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return root


def mergeTrees(t1, t2):
    if t1 and t2:
        root = TreeNode(t1.val + t2.val)
        root.right = self.mergeTrees(t1.right, t2.right)
        root.left = self.mergeTrees(t1.left, t2.left)
        return root
    return t1 or t2


def mergeTrees(t1, t2):
    if not t1: return t2;
    if not t2: return t1;
    t1.val += t2.val;
    t1.left = self.mergeTrees(t1.left, t2.left);
    t1.right = self.mergeTrees(t1.right, t2.right);
    return t1;
