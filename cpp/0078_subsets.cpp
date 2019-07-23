#https://leetcode.com/problems/subsets/

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<vector<int>> L;
        int n = nums.size();
        int size = 1 << n;
        
        for(int i = 0; i < size; i++)
        {
            vector<int> sub;
            for(int j = 0; j < n; j++) 
            {
                if( i & (1 << j)) { sub.push_back(nums[j]); }
            }
            L.push_back(sub);
        }
        return L;
    }
};


class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<vector<int>> res(1);
        
        for(int i = 0; i < nums.size(); i++)
        {
            int cnt = res.size();
            
            for(int j = 0; j < cnt; j++)
            {
                vector<int> temp = res[j];
                temp.push_back(nums[i]);
                res.push_back(temp);
            }
        }
        return res;
    }
};
