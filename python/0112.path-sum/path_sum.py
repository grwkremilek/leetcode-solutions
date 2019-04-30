#https://leetcode.com/problems/path-sum/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, summ):
    if not root:
        return False
    if not root.left and not root.right and root.val == summ:
        return True
    summ -= root.val
    return hasPathSum(root.left, summ) or hasPathSum(root.right, summ)
