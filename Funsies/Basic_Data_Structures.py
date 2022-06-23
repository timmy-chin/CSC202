class Node:
    def __init__(self, init_item):
        self.data = init_item
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        while current is not None and current.data != item:
            current = current.get_next()

        if current is None:
            return False

        elif current.data == item:
            return True

    def remove(self, item):
        current = self.head
        previous = None
        while current.data != item and current is not None:
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = current.get_next()

        elif current.data == item:
            previous.next = current.get_next()

    def pop(self, index=-1):
        current = self.head
        count = 0
        previous = None
        if index == -1:
            index = self.size() - 1

        while current is not None and count != index:
            previous = current
            current = current.get_next()
            count += 1

        if previous is None and current is None:
            self.head = None

        elif previous is None and count == 0:
            self.head = current.next

        elif count == index:
            previous.next = current.get_next()

        elif current is None:
            return 'Out of Range or Empty List'

    def insert(self, index, item):
        current = self.head
        count = 0
        previous = None
        while count != index and current is not None:
            count += 1
            previous = current
            current = current.get_next()

        if previous is None and count == 0:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

        elif count == index:
            temp = Node(item)
            temp.next = current
            previous.next = temp

        elif current is None:
            previous.next = Node(item)

    def index(self, item):
        current = self.head
        count = 0
        while current.next is not None and current.data != item:
            current = current.get_next()
            count += 1

        if current is None and count == 0:
            return "Empty List"

        elif current.data == item:
            return current.data

        elif current.next is None:
            return "Does Not Exist"

    def append(self, item):
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = Node(item)
        else:
            previous.next = Node(item)

    def isempty(self):
        return self.head is None

    def element(self, index):
        current = self.head
        count = 0
        previous = None
        while current is not None and count != index:
            previous = current
            count += 1
            current = current.get_next()

        if previous == None and current is None:
            return 'Empty List'
        elif count == index:
            return current.data
        elif current is None:
            return 'Out of Range'

    def __repr__(self):
        str = '['
        current = self.head
        while current is not None:
            if current.next is None:
                str += f'{current.data}]'
            else:
                str += f'{current.data}, '
            current = current.get_next()
        return str


class List:
    def __init__(self, lst):
        self.list = UnorderedList()
        for i in range(len(lst)):
            self.list.add(lst[len(lst) - 1 - i])

    def size(self):
        return self.list.size()

    def remove(self, item):
        self.list.remove(item)

    def search(self, item):
        return self.list.search(item)

    def pop(self, index=-1):
        return self.list.pop(index)

    def insert(self, index, item):
        self.list.insert(index, item)

    def index(self, item):
        return self.list.index(item)

    def append(self, item):
        self.list.append(item)

    def isempty(self):
        return self.list.isempty()

    def element(self, index):
        return self.list.element(index)

    def __repr__(self):
        str = '['
        list = self.list
        current = list.head
        while current is not None:
            if current.next is None:
                str += f'{current.data}]'
            else:
                str += f'{current.data}, '
            current = current.get_next()
        return str


class Stack:
    def __init__(self):
        self.stack = List([])

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        num = self.stack.size()
        element = self.stack.element(num - 1)
        self.stack.pop()
        return element

    def peek(self):
        num = self.stack.size()
        return self.stack.element(num - 1)

    def isempty(self):
        return self.stack.list.isempty()

    def size(self):
        return self.stack.size()

    def __repr__(self):
        str = '['
        Lst = self.stack
        ULst = Lst.list
        current = ULst.head
        while current is not None:
            if current.next is None:
                str += f'{current.data}]'
            else:
                str += f'{current.data}, '
            current = current.get_next()
        return str


class Queue:
    def __init__(self):
        self.queue = List([])

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        num = self.queue.size()
        element = self.queue.element(num - 1)
        self.queue.pop()
        return element

    def isempty(self):
        return self.queue == []

    def size(self):
        return self.queue.size()

    def __repr__(self):
        str = '['
        Lst = self.queue
        ULst = Lst.list
        current = ULst.head
        while current is not None:
            if current.next is None:
                str += f'{current.data}]'
            else:
                str += f'{current.data}, '
            current = current.get_next()
        return str


class Deque:
    def __init__(self):
        self.deque = List([])

    def add_rear(self, item):
        self.deque.insert(0, item)

    def add_front(self, item):
        self.deque.append(item)

    def remove_rear(self):
        element = self.deque.element(0)
        self.deque.pop(0)
        return element

    def remove_front(self):
        num = self.deque.size()
        element = self.deque.element(num - 1)
        self.deque.pop()
        return element

    def size(self):
        return self.deque.list.size()

    def __repr__(self):
        str = '['
        Lst = self.deque
        ULst = Lst.list
        current = ULst.head
        while current is not None:
            if current.next is None:
                str += f'{current.data}]'
            else:
                str += f'{current.data}, '
            current = current.get_next()
        return str


class OrderedList(UnorderedList):
    def search(self, item):
        current = self.head
        while current.data != item and current.data < item:
            current = current.get_next()

        if current.data == item:
            return True
        else:
            return False

    def add(self, item):
        current = self.head
        previous = None
        while current is not None and current.data < item:
            previous = current
            current = current.get_next()

        if previous is None:
            temp = Node(item)
            temp.next = current
            self.head = temp
        else:
            temp = Node(item)
            temp.next = current
            previous.next = temp

# Testing for List
# lst = List([1,2,3,4,5,6,7,8,9,10])
# print(lst)
# print(lst.size())
# lst.pop(1)
# print(lst)
# lst.pop()
# print(lst)
# lst.remove(3)
# print(lst)
# lst.append(6)
# print(lst)
# print(lst.index(2))
# print(lst.isempty())
# print(lst.search(5))
# print(lst.search(10))
# lst.insert(3,8)
# print(lst)
# print(lst.pop(100))


# Testing for Stack
# s = Stack()
# s.push(5)
# s.push(6)
# s.push(7)
# print(s.peek())
# print(s.pop())
# print(s.isempty())
# print(s.size())
# print(s)

# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q)
# print(q.dequeue())
# print(q)

# d = Deque()
# d.add_rear(10)
# d.add_rear(20)
# d.add_front(5)
# d.add_front(7)
# print(d)
# print(d.remove_front())
# print(d.remove_rear())
# print(d)

# olst = OrderedList()
# olst.add(4)
# olst.add(6)
# olst.add(2)
# olst.add(7)
# olst.add(5)
# olst.add(3)
# print(olst)


def pcd(str):
    dict = {"(": '1', "+": '2', "-": '2', "*": '3', "/": '3'}
    return dict[str]

def postfix(str):
    s = Stack()
    exp = UnorderedList()
    for letter in str:
        if letter.isalpha() or letter.isdigit():
            exp.append(letter)
        elif letter == ')':
            while s.peek() != '(':
                exp.append(s.pop())
            s.pop()
        elif pcd(letter) > s.peek() or s.peek() == 'Empty List':
            s.push(letter)
    while not s.isempty():
        exp.append(s.pop())

    return exp

def potato_game(name_list, num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() != 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

def palindrome(str):
    d = Deque()
    for letter in str:
        d.add_front(letter)
    num = d.size()
    while num > 1:
        if d.remove_rear() != d.remove_front():
            return False
        num = d.size()
    return True






