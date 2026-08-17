class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int max_len = 1;
        int state = 0;
        int l = 0; 
        
        for (int r = 0; r < nums.size(); ++r) {
            while ((state & nums[r]) != 0) {
                state ^= nums[l];
                l++;              
            }
            
            state |= nums[r];
            
            max_len = max(max_len, r - l + 1);
        }
        
        return max_len;
    }
};