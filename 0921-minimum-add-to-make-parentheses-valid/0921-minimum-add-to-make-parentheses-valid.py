class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i=="(":
                stack.append(i)
            elif i==")":
                if len(stack)!=0 and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)