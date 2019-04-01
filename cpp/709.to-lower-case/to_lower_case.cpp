//https://leetcode.com/problems/to-lower-case/

class Solution {
public:
    string toLowerCase(string str) 
    {
        for(char &c : str)
        {
            if ('A' <= c && c <= 'Z')
            {
                c += 32;
            }
        }
        return str;
    }
};
