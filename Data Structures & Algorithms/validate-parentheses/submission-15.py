class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        if(len(s) == 1):
            return False

        verdict = True

        for i in range((len(s))):
            if(s[i:i+1] == "(" or s[i:i+1] == "[" or s[i:i+1] == "{"):
                stack.append(s[i:i+1])
            else:
                if(len(stack) == 0):
                    return False
                st = stack.pop()
                if( st == "(" and s[i:i+1] != ")"):
                    verdict = False
                elif( st == "[" and s[i:i+1] != "]"):
                    verdict = False
                elif( st == "{" and s[i:i+1] != "}"):
                    verdict = False
        if(len(stack) != 0):
            verdict = False


        return verdict
            
            

        