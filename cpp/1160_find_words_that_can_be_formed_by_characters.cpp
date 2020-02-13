//https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        
        int count = 0;
        unordered_map<char,int> mp;
        
        for(int i=0; i<chars.size(); i++) { mp[chars[i]]++; }
        
        for(string word : words)
        {
            bool match = true;
            unordered_map<char, int> temp = mp;
            
            for(char ch : word) { if(temp[ch]-- <= 0) { match = false; break; } }
            
            if(match) { count += word.length(); } 
        }
        
        return count;
    }
};
