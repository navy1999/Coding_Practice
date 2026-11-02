class Solution:
    def isValid(self, s: str) -> bool:
        pairs= {']' : '[' ,'}' :'{' ,')':'('}
        stack=[]
        for c in s:
            if (c=='[' or c == '{' or c=='(' ):
                stack.append(c)
            elif (stack and stack[-1] == pairs[c]):
                stack.pop()
            else: 
                return False
        
        return len(stack) ==0
