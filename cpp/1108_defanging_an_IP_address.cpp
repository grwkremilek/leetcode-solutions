//https://leetcode.com/problems/defanging-an-ip-address/submissions/

class Solution {
public:
    string defangIPaddr(string address) 
    {
        std::string out;
        std::string in = "[.]";
        for (const auto& i : address) 
        {
            if (i == '.') { out += in; }
            else { out += i; }
        }
        return out; 
    }
};
