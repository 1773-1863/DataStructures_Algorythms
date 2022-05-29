class Node:
    def __init__(self, value):
        """ initializing a node with the parameter {value}"""
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
    # create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """this function prints all elements of the linked list"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """this function add an element to the end of the linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """this function remove the the last element of the linked list"""
        if self.length == 0:
            print("there is Linked List element to pop, first you need to create one")
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
            print("there is no Linked List element to pop, first you need to create one")
        return temp.value

    def prepend(self, value):
        """this function add an element to the head of the linked list"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        """this function remove the first element of the linked list"""
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """this function return the value of the node which has the parameter index in the linked list"""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, value, index):
        """this function set the value of the node with the index in the linked list"""

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        """this function insert a node to the the place with the index in the linked list"""
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """this function remove the node which is specified with the index parameter"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """this function reverse the linked list"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList("xx")
my_linked_list.append(3)
my_linked_list.append(6)
my_linked_list.append(8)
my_linked_list.append(12)
print(f"Tail Value: {my_linked_list.tail.value}")
print(f"Linked List Length: {my_linked_list.length}")
print("-------POP FUNCTION OF LINKED LIST-------")
my_linked_list.pop()
print(f"Tail Value: {my_linked_list.tail.value}")
print(f"Linked List Length: {my_linked_list.length}")
print("-------PREPEND FUNCTION OF LINKED LIST-------")
my_linked_list.prepend(1)
print(f"Head Value: {my_linked_list.head.value}")
print(f"Linked List Length: {my_linked_list.length}")
print("-------POP_FIRST FUNCTION OF LINKED LIST-------")
my_linked_list.pop_first()
print(f"Head Value: {my_linked_list.head.value}")
print(f"Linked List Length: {my_linked_list.length}")
print(my_linked_list.get(2).value)
print("-------SET FUNCTION OF LINKED LIST-------")
my_linked_list.set("xxx!!!", 2)
my_linked_list.print_list()
print("-------INSERT FUNCTION OF LINKED LIST-------")
my_linked_list.insert("!!!", 0)
my_linked_list.print_list()
print("-------REMOVE FUNCTION OF LINKED LIST-------")
my_linked_list.remove(2)
my_linked_list.print_list()
print("-------REVERSE FUNCTION OF LINKED LIST-------")
my_linked_list.reverse()
my_linked_list.print_list()