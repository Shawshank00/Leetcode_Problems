class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {')':'(', '}':'{', ']':'['}
        stk =[]

        for p in s:
            if p not in hashmap:
                stk.append(p)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[p]:
                        return False
        return not stk

            


            
            
        
        


        
