//https://leetcode.com/problems/permutations/

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        
        vector<std::vector<int>> result;
        vector<int> path;
        dfs(nums, 0, result);
        return result;
    }
    
    void dfs(vector<int>& nums, int pos, vector<std::vector<int>>& result)
    {
        if(pos>=nums.size()) { result.push_back(nums); return; }
        for(int i=pos; i<nums.size(); i++)
        {
            swap(nums[pos], nums[i]);
            dfs(nums, pos+1, result);
            swap(nums[pos], nums[i]);
        }
    }
};
