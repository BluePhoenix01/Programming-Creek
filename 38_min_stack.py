class MinStack:
    def __init__(self, val = None):
        self.stack = []
        self.top = 1 if val else 0 
        self.min = val if val else None
        
    def push(self, val):
        self.stack.append(val)
        self.top += 1
        if not self.min:
            self.min = val
        else:
            self.min = min(self.min, val)
    
    def pop(self):
        self.stack.pop()
        self.top -= 1
    
    def get_min(self):
        return self.min

    def get_top(self):
        return self.stack[self.top-1]

stackA = MinStack()
stackA.push(5)
stackA.push(2)
stackA.push(8)
stackA.push(1)
stackA.push(3)

print("Minimum value in stack:", stackA.get_min())
print("Top value in stack:", stackA.get_top())

stackA.pop()
print("Top value in stack after pop:", stackA.get_top())