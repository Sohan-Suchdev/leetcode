class Solution {
private:
    double dfs(string current, string target, unordered_set<string>& visited, unordered_map<string, vector<pair<string, double>>>& adjList) {
            if (adjList.find(current) == adjList.end() || adjList.find(target) == adjList.end()) {
                return -1.0;
            }
            if (visited.count(current)>=1){
                return -1;
            } else if (current == target){
                return 1;
            }

            visited.insert(current);

            for (auto& neighbor_pair : adjList[current]){
                string neighbor = neighbor_pair.first;
                double weight = neighbor_pair.second;

                if (visited.count(neighbor) == 0) {
                double result = dfs(neighbor, target, visited, adjList);
                
                    if (result != -1.0) {
                        return weight * result;
                    }
                }

            }
            return -1.0;
        }
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int len = equations.size();
        unordered_map<string, vector<pair<string, double>>> adjList;

        for (int i = 0; i < len; ++i) {
            adjList[equations[i][0]].push_back({equations[i][1], values[i]});
            adjList[equations[i][1]].push_back({equations[i][0], 1.0 / values[i]});
        }

        int len_queries = queries.size();
        vector<double> res(len_queries, 0);

        for (int i = 0; i<len_queries; ++i){
            unordered_set<string> visited;
            res[i] = dfs(queries[i][0], queries[i][1], visited, adjList);
        }

        return res;
    }
};