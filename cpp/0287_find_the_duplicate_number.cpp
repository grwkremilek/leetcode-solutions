//https://leetcode.com/problemset/all/

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int slow = nums[0];
        int fast = nums[nums[0]]; 
        int finder = 0;
        
        while (slow != fast) 
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        
        while (slow != finder)
        {
            slow = nums[slow];
            finder = nums[finder];
        }
        
        return finder;
    }
};


class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int left = 0;
        int right = nums.size();
        
        while(left < right){
            int mid = left + (right -  left)/2;
            int count = 0;
            
            for(int num :nums)
            {
                if(num <= mid){ count++; }
            }
            if(count <= mid){ left = mid + 1; }
            else { right = mid; }
        }
        return right;
    }
};
