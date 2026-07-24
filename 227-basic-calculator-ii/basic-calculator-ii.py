class Solution:
    def calculate(self, s: str) -> int:
        res = 0         
        curr_term = 0   
        curr_num = 0
        op = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)
            
            if char in "+-*/" or i == len(s) - 1:
                if op == '+':
                    res += curr_term      
                    curr_term = curr_num  
                elif op == '-':
                    res += curr_term    
                    curr_term = -curr_num  
                elif op == '*':
                    curr_term *= curr_num  
                elif op == '/':
                    curr_term = int(curr_term / curr_num) 
                
                op = char
                curr_num = 0
                
        return res + curr_term