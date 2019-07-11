class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        
        vector<int> odd;
        vector<int> even;
        
        for(auto&& a: A)
        {
            if (a % 2 == 0) {
                odd.push_back(a); 
            } else {
                even.push_back(a);
            }
        }
        odd.insert(std::end(odd), std::begin(even), std::end(even));
        return odd;
    }
};


class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        auto is_even = [] (auto e) { return e % 2 == 0; };
        partition (A.begin (), A.end (), is_even);
        return A;
    }
}; 
