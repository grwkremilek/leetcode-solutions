//https://leetcode.com/problems/fizz-buzz/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        std::vector<std::string> ans;
        
        for(int i=1; i <= n; i++){
            if (i%15 == 0){ ans.push_back("FizzBuzz"); }
            else if (i%3 == 0){ ans.push_back("Fizz"); }
            else if (i%5 == 0){ ans.push_back("Buzz"); }
            else { ans.push_back(std::to_string(i)); }
        }
       return ans; 
    }
};
