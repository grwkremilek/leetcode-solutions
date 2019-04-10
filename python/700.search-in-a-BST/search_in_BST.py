#https://leetcode.com/problems/search-in-a-binary-search-tree/

def searchBST(root, val):
        if root is None or root.val == val: 
            return root
        if root.val < val: 
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
