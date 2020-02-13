//https://leetcode.com/problems/unique-email-addresses/

class Solution {
public:
    string reverseWords(string s) {
        
        int i = 0, j = 0, k;
        
        while(j < s.size()) 
        {
            i = j;
            while(s[j] != ' ' && j < s.size()) j++;
            k = j-1;
            while(i < k) swap(s[i++], s[k--]);
            j++;
        }
        return s; 
    }
};
