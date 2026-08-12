class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total_sum = accumulate(nums.begin(), nums.end(), 0);
        if (total_sum % 2 != 0) {
            return false;
        }
        int target = total_sum / 2;
        
        vector<bool> dp(target + 1, false);
        dp[0] = true; 
        
        for (int num : nums) {
            for (int current_sum = target; current_sum >= num; current_sum--) {
                if (dp[current_sum - num]) {
                    dp[current_sum] = true;
                }
            }
        }
        
        return dp[target];      
    }
};
