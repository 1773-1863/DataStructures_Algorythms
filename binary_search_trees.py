# Full tree - all arrows are filled
# Perfect tree - all nodes are filled at the level of maximum
# complete tree -
# parent and child nodes(siblings) every node has just one parent
# each bottom node is called leaf

# --------------- BINARY SEARCH TREE --------------- #
# 1.0 Preview :
# BIG O : 2^n-1 approx. 2^n == O(log n) aka divide and conquer
# if tree never forks it will be linked list
# worst case is never forked tree, in other words linked list, at this situation O(n)
# insert is faster in linked list, lookup and remove are faster in BST

# 1.1 Constructor

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: # equality
                return True
        return False

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node



print("-----------------------  INIT / BST -----------------------")
my_tree = BinarySearchTree()
print("-----------------------  INSERT / BST -----------------------")
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
print("-----------------------  CONTAINS / BST -----------------------")
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(27))
print(my_tree.contains(17))
print("-----------------------  MIN VALUE / BST -----------------------")
print(my_tree.min_value(my_tree.root).value)
print(my_tree.min_value(my_tree.root.right).value)

