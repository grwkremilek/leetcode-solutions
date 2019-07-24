#https://leetcode.com/problems/length-of-last-word/

class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int i = 0, j = s.length() - 1;
        
        while (j >= 0 && s[j] == ' ') { j--; }
        while (j >= 0 && s[j] != ' ') { i++; j--; }
        
        return i;       
    }
};
