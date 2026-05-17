class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid = True
        for i in range(len(s)):
            if(s[i] == "("):
                stack.append("(")
            if(s[i] == "{"):
                stack.append("{")
            if(s[i] == "["):
                stack.append("[")

            if(s[i] == ")"):
                if(len(stack) == 0 or stack.pop() != "(" ):
                    valid = False
            if(s[i] == "}"):
               if(len(stack) == 0 or stack.pop() != "{" ):
                    valid = False
            if(s[i] == "]"):
                if(len(stack) == 0 or stack.pop() != "[" ):
                    valid = False

        if(len(stack) != 0):
            valid = False
            

        return  valid

        