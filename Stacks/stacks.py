class stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)
    def peek(self):
        if len(self.s)==0:
            return("stack is empty")
        else :
            return self.s[0]
        
    def pop(self):
        if len(self.s)==0:
            return("Stack is EMpty")
        else:
            return self.s.pop(0)
stk=stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
