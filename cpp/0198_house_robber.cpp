#https://leetcode.com/problems/house-robber/

class Solution {
public:
    int rob(vector<int>& nums) {
        
        int last = 0, cur = 0;
        for (int i = 0; i < nums.size(); i++) 
        { 
            last = max(last + nums[i], cur);
            swap(last, cur);
        }
        return cur;
    }
};


class Solution {
public:
    vector<int> ret;
    
    int solve(int idx, vector<int>& nums)
    {
        if (idx < 0) { return 0; }
        if (ret[idx] >= 0) { return ret[idx]; }
        ret[idx] = max(nums[idx] + solve(idx-2, nums), solve(idx-1, nums));
        return ret[idx];
    }
    
    int rob(vector<int>& nums) 
    {
        for(int i = 0; i < nums.size(); ++i) { ret.push_back(-1); }
        return solve(nums.size()-1, nums);
    }
};
