#https://leetcode.com/problems/generate-parentheses/

class Solution {
public:
    vector<string> generateParenthesis(int n) {

        vector<string> ans;
        generateParentheses(ans, "", n, n);
        return ans;
    }
    
    void generateParentheses ( vector<string> & res, string str, int left, int right ) {
        
        if(left == 0 && right == 0) { res.push_back(str); return; }
        if(left > 0)                { generateParentheses(res, str + "(", left - 1, right); }
        if(right > left)            { generateParentheses(res, str + ")", left, right - 1); }
    }
};
