#https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {

        vector<int> results;

        int pLen = p.length();
        int sLen = s.length();
        if (pLen > sLen) { return results; }

        vector<int> ps(26, 0);
        vector<int> ss(26, 0);
        
        for (int i = 0; i < pLen; ++i)
        {
            int pi = p[i];
            int si = s[i];
            ps[pi-97] += 1;
            ss[si-97] += 1;
        }

        if (ps == ss) { results.push_back(0); }

        for (int i = pLen; i < sLen; i++) 
        {
            int si = s[i];
            int sip = s[i-pLen];
            ss[si-97] += 1;
            ss[sip-97] -= 1;
            if (ps == ss) { results.push_back(i - pLen + 1); }
        }         

        return results;
    }
};
