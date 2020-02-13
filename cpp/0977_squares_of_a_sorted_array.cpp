//https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        
        std::vector<int> result(A.size());
        int l = 0; int r = A.size()-1;
        
        for(int i = A.size()-1; i >= 0; --i)
        {
            if (A[l]*A[l] > A[r]*A[r]) { result[i] = A[l]*A[l]; l++; }
            else  { result[i] = A[r]*A[r]; r--; }
            
        }
        return result; 
    }
};
