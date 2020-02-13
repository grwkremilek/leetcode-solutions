//https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
public:
    int minimumSwap(string s1, string s2) {
        
        int x = 0;
        int y = 0;
        
        for (int i = 0; i < s1.size(); i++) 
        {
            if (s1[i] != s2[i] and s1[i] == 'x') { x++; }
            if (s1[i] != s2[i] and s1[i] == 'y') { y++; }   
        }
    
        if ((x + y) % 2 != 0) { return -1; }
            
        return x/2 + y/2 + 2 * (x % 2);

    }
};
