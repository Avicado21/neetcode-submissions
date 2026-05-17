class Solution:
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):

            if self.is_number(tokens[i]):
                stack.append(float(tokens[i]))
            else:
                if(tokens[i] == "+"):
                        num = stack.pop() + stack.pop()
                        stack.append(num)
                if(tokens[i] == "-"):
                        num1 = stack.pop() 
                        num2 = stack.pop()
                        num = num2-num1
                        stack.append(num)

                if(tokens[i] == "*"):
                    num = stack.pop() * stack.pop()
                    stack.append(num)

                if(tokens[i] == "/"):
                    num1 = stack.pop() 
                    num2 = stack.pop()
                    num = int(num2/num1)
                    stack.append(num)

        return math.ceil(stack.pop())

        