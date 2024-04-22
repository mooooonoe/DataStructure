mylist = [1, 2, 3, 4, 5]

def myfun(self, *args):
    print(args[0])  # args의 첫 번째 요소를 출력합니다.
    print(len(args))  # args의 길이를 출력합니다.

myfun(mylist)




# linked queue로 구현 
class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):
        self.item = newItem
        self.next = nextNode


class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i: int, newItem) -> None:
        if 0 <= i <= self.__numItems:
            prev = self.getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None

        if len(args) != 0:
            i = args[0]

        if len(args) == 0 or i == -1:
            i = self.__numItems - 1

        if 0 < i <= self.__numItems - 1:
            prev = self.getNode(i - 1)
            retItem = prev.next.item
            prev.next = prev.next.next
            if i == self.__numItems - 1:
                self.__tail = prev

            self.__numItems -= 1
            return retItem
        else:
            return None

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def get(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        if 0 <= i <= self.__numItems - 1:
            return self.getNode(i).item
        else:
            return None

    def getNode(self, i: int) -> ListNode:
        curr = self.__tail.next
        for idx in range(i + 1):
            curr = curr.next
        return curr

    def __iter__(self):
        return CircularLinkedListIterator(self)

    def size(self) -> int:
        return self.__numItems
    
class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item


class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()

    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)

    def printQ(self):
        print("Queue from front:", end=' ')
        for i in range(self.__queue.size()):
            print(self.__queue.get(i), end=' ')
        print()

    def isEmpty(self) -> bool:
        return self.__queue.isEmpty()


class Deque:
    def __init__(self):
        self.__deque = LinkedQueue()
        self.__numItems = 0

    def addtop(self, x):
        self.__deque.enqueue(x)
        self.__numItems += 1
    
    def deltail(self):
        self.__deque.dequeue()
        self.__numItems -= 1

    def size(self):
        return self.__numItems
    
    def printDeque(self):
        print("Deq form front: ", end = ' ')
        for i in range(self.size()):
            print(self.__deque.get(i), end=' ')
        print()

    def isEmpty(self) -> bool:
        return self.__deque.isEmpty()