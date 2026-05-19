class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp = []

        for op in operations:
            if op == "+":
                num = int(temp[-2])+int(temp[-1])
                temp.append(num)
            elif op == "D":
                num = 2*int(temp[-1])
                temp.append(num)
            elif op == "C":
                temp.pop()
            else:
                temp.append(int(op))
        
        return sum(temp)
        