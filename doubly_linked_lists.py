class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        """ this function creates a doubly linked list"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """ this function prints all elements of the doubly linked list"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """ this function adds a node with the parameter value to the doubly linked list"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """ this function removes the last node of the doubly linked list"""
        if self.tail is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            # temp.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """ this function removes the first node of the doubly linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.prev = None
            self.head.next = temp
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        """ this function returns the node with the index value of the doubly linked list"""
        if index < 0 or index > self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            """ for efficiancy we use the two tails of doubly linked list"""
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """ this function changes the node value with the parameter value with the the help of index parameter"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    def insert(self, index, value):
        """ this function insert the node with the parameter value and  with the help of index parameter"""

        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        """ this function removes the node with the help of index parameter in the doubly linked list"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

print("--------- CREATE A DOUBLY LINKED LIST ---------")
m_doubly_linked_list = DoublyLinkedList(7)
m_doubly_linked_list.print_list()
print("--------- APPEND / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.append(2)
m_doubly_linked_list.print_list()
print("--------- POP / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.pop()
m_doubly_linked_list.print_list()
print("--------- PREPEND / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.prepend(5)
m_doubly_linked_list.print_list()
print("--------- POP FIRST / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.pop_first()
m_doubly_linked_list.print_list()
print("--------- GET / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.append(1)
m_doubly_linked_list.append(9)
m_doubly_linked_list.append(8)
print(m_doubly_linked_list.get(3).value)
print("--------- SET / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.set_value(0,"xx")
m_doubly_linked_list.print_list()
print("--------- INSERT / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.insert(2, "xxx")
m_doubly_linked_list.print_list()
print("--------- REMOVE / DOUBLY LINKED LIST ---------")
m_doubly_linked_list.remove(2)
m_doubly_linked_list.print_list()