#https://leetcode.com/problems/path-sum-ii/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum(root, summ):
    if not root:
        return []
    if root.left == None and root.right == None:
        if sum == root.val: 
            return [[root.val]] 
    tmp = pathSum(root.left, sum - root.val) + pathSum(root.right, sum - root.val)
    return [[root.val] + t for t in tmp]
