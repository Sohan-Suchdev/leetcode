class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        vector<int> freq (26, 0);

        for (char chr : s){
            freq[chr-'a']++;
        }

        string result = "";
        int curr = 25;
        
        while (curr >= 0) {
            if (freq[curr] == 0) {
                curr--;
                continue;
            }
            
            int use = min(freq[curr], repeatLimit);
            result.append(use, curr + 'a');
            freq[curr] -= use;
            
            if (freq[curr] > 0) {
                int next_char = curr - 1;
                
                while (next_char >= 0 && freq[next_char] == 0) {
                    next_char--;
                }
                
                if (next_char < 0) {
                    break;
                }
                
                result.push_back(next_char + 'a');
                freq[next_char]--;
            }
        }
        
        return result;        
    }
};