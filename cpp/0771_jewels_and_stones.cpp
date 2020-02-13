//https://leetcode.com/problems/jewels-and-stones/

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        
        int count = 0;
        
        for(auto&& s: S)
        {
            if (J.find(s) != std::string::npos) { ++count; }   
        }
        return count;
    }
};
