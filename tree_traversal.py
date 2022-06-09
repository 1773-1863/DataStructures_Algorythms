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

    def bfs(self):
        """breadth first search"""
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def dfs_pre_order(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_post_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def dfs_in_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result





print("-----------------------   BREADTH SEARCH/ TREE TRAVERSAL -----------------------", "\n")
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
print(my_tree.bfs(), "\n")
print("----------------------- DEPTH FIRST SEARCH_PRE_ORDER / TREE TRAVERSAL -----------------------", "\n")
print(my_tree.dfs_pre_order())
print("----------------------- DEPTH FIRST SEARCH_POST_ORDER / TREE TRAVERSAL -----------------------", "\n")
print(my_tree.dfs_post_order())
print("----------------------- DEPTH FIRST SEARCH_IN_ORDER / TREE TRAVERSAL -----------------------", "\n")
print(my_tree.dfs_in_order())