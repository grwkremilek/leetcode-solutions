//https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        
        int end = 0, m1 = nums[0];
        
        for (int i = 1; i < nums.size(); i++) 
        {
            if (nums[i] < m1) { end = i + 1; }
            else { m1 = nums[i]; }
        }

        int start = nums.size(), m2 = nums[nums.size() - 1];
        
        for (int i = nums.size() - 2; i >= 0; i--) 
        {
            if (nums[i] > m2) { start = i; }
            else { m2 = nums[i]; }
        }

        return max(end - start, 0);
    }
};
