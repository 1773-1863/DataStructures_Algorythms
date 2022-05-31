# --------------------- STACKS ------------------------#

# LIFO : Last in first out rule, O(n)
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp= self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

# ----------- FIFO : First in first out ---------------------- #
# inqueue : adding element to the queue
# dequeue : removing element from the queue
# O(1) - O(n)

class Queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1




print("---------------- INITIALIZE / STACK ----------------")
my_stack = Stack(2)
my_stack.print_stack()
print("---------------- PUSH / STACK ----------------")
my_stack.push(1)
my_stack.print_stack()
print("---------------- POP / STACK ----------------")
my_stack.pop()
my_stack.print_stack()
print("---------------- INITIALIZE / QUEUE ----------------")
my_queue = Queue(4)
my_queue.print_queue()
print("---------------- ENQUEUE / QUEUE ----------------")
my_queue.enqueue(7)
my_queue.print_queue()
print("---------------- DEQUEUE / QUEUE ----------------")
my_queue.dequeue()
my_queue.print_queue()
print("---------------- DEQUEUE / QUEUE ----------------")
my_queue.dequeue()
print(my_queue.print_queue())
