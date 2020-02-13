//https://leetcode.com/problems/search-in-a-binary-search-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {  
        if(!root) return NULL;
        if(root->val==val) return root;
        else return root->val<val ? searchBST(root->right,val) : searchBST(root->left,val);
    }
};
