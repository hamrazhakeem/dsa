class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
    def display(self):
        for item in self.items:
            print(item)

q = Queue()
q.display()
q.enqueue(10)
q.enqueue(59)
q.enqueue(50)
print("Dequeued item: ", q.dequeue())
print(q.is_empty())
print(q.peek())