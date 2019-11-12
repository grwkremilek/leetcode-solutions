#https://leetcode.com/problems/intersection-of-two-arrays/


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        std::vector<int> res;
        int i = 0; int j = 0;
        std::sort(nums1.begin(), nums1.end(), std::less<int>());
        std::sort(nums2.begin(), nums2.end(), std::less<int>());
        
        while (i < nums1.size() and j < nums2.size())
        {
            if (nums1[i] > nums2[j])        { j++; }
            else if (nums1[i] < nums2[j])   { i++; }          
            else {
                    if (not (res.size() and nums1[i] == res[res.size()-1])) { res.push_back(nums1[i]); }
                    i++;
                    j++;
                }
            }
        return res;
    }
};


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> m(nums1.begin(), nums1.end());
        std::vector<int> res;
        for (auto n : nums2)
        {
            if (m.count(n))
            {
                res.push_back(n);
                m.erase(n);
            }
        }
        return res;
    }
};


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size();
        int n2=nums2.size();
        vector<int> res={};
        
        for(int i =0;i<n1;i++){
            for(int j = 0;j<n2;j++){
                if ( nums1[i] == nums2[j] ){
                    if (!(std::find(res.begin(), res.end(), nums1[i]) != res.end())) {
                        res.push_back(nums1[i]);
                        break;
                    }
                }
            }
        }
        return res;
    }
};
