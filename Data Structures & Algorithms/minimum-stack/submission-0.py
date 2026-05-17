class MinStack:
    stack = []
    length = 0


    def __init__(self):
        self.stack =  []
        self.length = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length +=1
        return None
        

    def pop(self) -> None:
        self.stack.pop()
        self.length-=1
        return None
        

    def top(self) -> int:
        return self.stack[self.length-1]
        

    def getMin(self) -> int:
        return sorted(self.stack)[0]
        
