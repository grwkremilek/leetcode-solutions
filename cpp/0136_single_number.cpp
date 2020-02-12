//https://leetcode.com/problems/single-number/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) { ans = ans xor nums[i]; }
        return ans;
    }
};


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        int xr = 0;
        for (int i = 0;i<n;++i) xr ^= nums[i];
        return xr;
    }
};
