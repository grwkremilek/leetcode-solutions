//https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
public:
    int balancedStringSplit(string s) {
        int countL = 0, countR = 0, out = 0;
        for (const auto& i : s) 
        {
            if (i == 'L') { countL += 1; }
            else if (i == 'R') { countR += 1; }

            if (countR == countL) { out += 1; }
        }    
        return out;
    }
};
