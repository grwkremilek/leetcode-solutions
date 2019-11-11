#https://leetcode.com/problems/unique-number-of-occurrences/

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        unordered_map<int, int> counts;
        unordered_set<int> s;
  
        for (auto a : arr)      { ++counts[a]; }
        for (auto& p : counts)  { s.insert(p.second); }
        return counts.size() == s.size();
    }
};
