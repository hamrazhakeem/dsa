class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def display(self):
        for item in reversed(self.items):
            print(item)

stack = Stack()
stack.push(10)
stack.push(30)
stack.push(70)
print(stack.peek())
print('popped item is: ',stack.pop())
stack.display()
print(stack.is_empty())