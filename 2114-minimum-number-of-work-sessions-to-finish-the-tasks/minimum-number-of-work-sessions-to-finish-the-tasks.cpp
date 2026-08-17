class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        int max_mask = 1 << n;
        vector<pair<int, int>> dp(max_mask, {n + 1, 0});

        dp[0] = {1, 0};
        
        for (int mask = 1; mask < max_mask; ++mask) {
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    int prev_mask = mask ^ (1 << i); 
                    auto [prev_sessions, prev_time] = dp[prev_mask];
                    
                    pair<int, int> next_state;
                    
                    if (prev_time + tasks[i] <= sessionTime) {
                        next_state = {prev_sessions, prev_time + tasks[i]};
                    } 
                    else {
                        next_state = {prev_sessions + 1, tasks[i]};
                    }
                    
                    dp[mask] = min(dp[mask], next_state);
                }
            }
        }
        
        return dp[max_mask - 1].first;
    }
};