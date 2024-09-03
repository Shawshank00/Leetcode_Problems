class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for i in operations:
            
            if i == "+":
                if len(arr) >= 2:
                    arr.append(arr[-1] + arr[-2])
            elif i == 'D':
                arr.append(arr[-1] * 2)
            elif i == 'C':
                if arr:
                    arr.pop()
            else:
                arr.append(int(i))
        return sum(arr)
            
