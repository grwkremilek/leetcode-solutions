//https://leetcode.com/problems/unique-morse-code-words/

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        
        vector<string> morse = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        unordered_set<string> trans;
        for (auto w : words) 
        {
            string code;
            for (auto c : w) { code += morse[c - 'a']; }
            trans.insert(code);
        }
        return trans.size();
    } 
};
