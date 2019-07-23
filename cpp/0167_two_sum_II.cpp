#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int l = 0, r = numbers.size() -1;
        
        while(l < r){
            
            int res = numbers[l] + numbers[r];
            
            if(res == target)       { return vector<int>{l+1, r+1}; }
            else if (res > target)  { r--; }
            else                    { l++; }
        }
        return {};
    }
};
