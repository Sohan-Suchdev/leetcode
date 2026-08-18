class Solution {
public:
void dfs(int curr, int current_dist, const vector<int>& edges, vector<int>& dist) {
        if (curr == -1) {
            return;
        }
        
        if (dist[curr] != -1) {
            return;
        }
        
        dist[curr] = current_dist;
        
        dfs(edges[curr], current_dist + 1, edges, dist);
    }
    
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        
        vector<int> dist1(n, -1);
        vector<int> dist2(n, -1);
        
        dfs(node1, 0, edges, dist1);
        dfs(node2, 0, edges, dist2);
        
        int min_score = INT_MAX;
        int best_node = -1;
        
        for (int i = 0; i < n; ++i) {
            if (dist1[i] != -1 && dist2[i] != -1) {
                int score = max(dist1[i], dist2[i]);
                
                if (score < min_score) {
                    min_score = score;
                    best_node = i;
                }
            }
        }
        return best_node;
    }
};