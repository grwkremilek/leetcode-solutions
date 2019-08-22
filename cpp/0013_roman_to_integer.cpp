#https://leetcode.com/problems/roman-to-integer/


class Solution {
public:
    int romanToInt(string s) {
        
        unordered_map<char, int> d = {   { 'I' , 1 },
                                         { 'V' , 5 },
                                         { 'X' , 10 },
                                         { 'L' , 50 },
                                         { 'C' , 100 },
                                         { 'D' , 500 },
                                         { 'M' , 1000 }   };
        int integers = 0;
        for(int i = 0; i < s.size(); i++)
        {
            if( i != s.size()-1 and d[s[i]] < d[s[i+1]]) { integers -= d[s[i]]; }
            else { integers += d[s[i]]; }
        }
        return integers;
    }
};



class Solution {
public:
    int romanToInt(string s) {
        
       int integers  = 0;
        for (int i = s.size() - 1; i >= 0; --i)
        {
            switch (s[i])
            {
                case 'I':
                    integers += integers >= 5 ? -1 : 1;
                    break;
                case 'V':
                    integers += 5;
                    break;
                case 'X':
                    integers += integers >= 50 ? -10 : 10;
                    break;
                case 'L':
                    integers += 50;
                    break;
                case 'C':
                    integers += integers >= 500 ? -100 : 100;
                    break;
                case 'D':
                    integers += 500;
                    break;
                case 'M':
                    integers += 1000;
                    break;
            }
        }
        return integers;
    }
};
