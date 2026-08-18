class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        sort(tiles.begin(), tiles.end());
        
        int n = tiles.size();
        int max_cover = 0;
        int current_cover = 0;
        int l = 0, r = 0;
        
        while (max_cover < carpetLen && r < n) {
            if (tiles[l][0] + carpetLen > tiles[r][1]) {
                current_cover += tiles[r][1] - tiles[r][0] + 1;
                max_cover = max(max_cover, current_cover);
                r++; 
            } 
            else {
                int partial_cover = max(0, tiles[l][0] + carpetLen - tiles[r][0]);
                max_cover = max(max_cover, current_cover + partial_cover);
                
                current_cover -= tiles[l][1] - tiles[l][0] + 1;
                l++; 
            }
        }
        
        return max_cover;
    }
};