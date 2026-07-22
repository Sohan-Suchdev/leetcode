import random

class RandomizedSet:
    def __init__(self):
        self.num_list = []    
        self.num_map = {}    

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
            
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
            
        idx_to_remove = self.num_map[val]
        
        last_val = self.num_list[-1]
        
        self.num_list[idx_to_remove] = last_val
        
        self.num_map[last_val] = idx_to_remove
        
        self.num_list.pop()
        del self.num_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)