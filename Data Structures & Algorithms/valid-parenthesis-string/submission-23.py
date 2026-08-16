class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        sStack = []

        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append((idx, ch))
            
            elif ch == "*":
                sStack.append((idx, ch))
            
            else:             
                if stack:
                    stack.pop()
                
                elif sStack:
                    sStack.pop()
                
                else:
                    return False
                
        if len(stack) > len(sStack):
            return False
        
        while stack:
            pIdx, p = stack.pop()
            sIdx, star = sStack.pop()
            if pIdx > sIdx:
                return False
        return True