class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        l = len(temp)
        arr = [0] * l
        stk = []

        for i, t in enumerate(temp):
            while stk and stk[-1][1] < t:
                stk_i, stk_t = stk.pop()
                arr[stk_i] = i - stk_i
            
            stk.append((i, t))
            
        return arr
