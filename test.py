# Queue 구현

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty() :
            return self.items.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.items)
    


queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print(queue.size())

for i in range(1,4):
    queue.enqueue(i)

print(queue.size())
print(queue.dequeue())

if queue.isEmpty():
    print('queue is empty !') 
else:
    print('queue is full !')


stack = []
stack.append(15)
stack.append(25)
stack.append(10)
stack.append(2)

print(stack)

i = stack.pop()
print(i)
print(stack)

