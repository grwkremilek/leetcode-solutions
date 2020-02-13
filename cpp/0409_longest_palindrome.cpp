//https://leetcode.com/problems/longest-palindrome/

class Solution {
public:
    int longestPalindrome(string s) {
        
        //create a hash table with frequencies
        unordered_map<char, int> freqs;
        for(char& c : s) { freqs[c]++; }
        
        //iterate values in the hash table
        int counts = 0;
        for(auto kv : freqs) { if (kv.second & 1) { counts++; } }
        return s.size() - counts + (counts >= 1);
    }
};
