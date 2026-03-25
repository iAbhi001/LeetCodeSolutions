class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        brackets={')':'(',']':'[','}':'{'}

        if len(s)==1:#if the length of string is 1,return False
            return False
        
        for i in s:
            if i in '([{': #if i is open,add i to stack
                stack.append(i)
            elif i in ')]}': #if it is close,check for empty stack or previous element in stack is matched to close brackets
                if not stack or stack[-1]!=brackets[i]:
                    return False
                stack.pop() 
        
        if len(stack)==0: #check the stack is empty or not
            return True
        return False

        

        
            
            