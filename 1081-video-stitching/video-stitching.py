class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        
        count = 0
        current_end = 0
        farthest_next = 0
        i = 0

        while current_end < time:
            while i < len(clips) and clips[i][0] <= current_end:
                farthest_next = max(farthest_next, clips[i][1])
                i += 1
            
            if current_end == farthest_next:
                return -1
                
            count += 1
            current_end = farthest_next
            
        return count