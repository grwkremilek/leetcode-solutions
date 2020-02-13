//https://leetcode.com/problems/robot-return-to-origin/

class Solution {
public:
    bool judgeCircle(string moves) {
        int horizontal = 0;
        int vertical = 0;
        
        for(char& m : moves)
        {
            if (m == 'L')       { horizontal++; }
            else if (m == 'R')  { horizontal--; }
            else if (m == 'U')  { vertical++; }
            else if (m == 'D')  { vertical--; }
        }
        return horizontal == 0 and vertical==0; 
    }
};



class Solution {
public:
    bool judgeCircle(string moves) {
        
        vector<int> counter(96, 0);
        
        for (char c : moves) { counter[c]++; }
        return counter['U'] == counter['D'] and counter['L'] == counter['R'];
    }
};
