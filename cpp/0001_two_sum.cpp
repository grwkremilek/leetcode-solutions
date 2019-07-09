class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> h;
        
        for (int i = 0;; ++i)
        {
            auto it = h.find(target - nums[i]);
            
            if (it != h.end()) 
                return vector<int> {i, it->second};
            
            h[nums[i]] = i;
        }
    }
};
