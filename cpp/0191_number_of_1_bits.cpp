//https://leetcode.com/problems/number-of-1-bits/

class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        if (n == 0) { return 0; }
        int count = 0;
        
        while (n != 1)
        {
            count += n % 2;
            n = n / 2;
        }
        return count + n;
        
    }
};
