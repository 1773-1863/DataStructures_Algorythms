# 1.0 - ABSTRACT
# one way, determenistic:every time same output with same input
# linear probing, open adressing : find empty cell
# hash tables have better performance if their size are equal to a prime number, this reduces collisions
# hashing is O(1), set is O(1), get O(n)


class HashTable():
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

def item_in_common(list1, list2):
    """ this function compare two list and return the common elements with O(n^2)"""
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common_efficient(list1, list2):
    """ this function compare two list and return the common elements with O(n)"""
    dict = {}
    for i in list1:
        dict[i] = True
    for j in list2:
        if j in dict:
            return True
    return False




print("-----------------------  INIT / HASH TABLES -----------------------")
my_hash_table = HashTable()
my_hash_table.print_table()
print("-----------------------  SET ITEM / HASH TABLES -----------------------")
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
my_hash_table.print_table()
print("-----------------------  GET ITEM / HASH TABLES -----------------------")
print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))
print("-----------------------  KEYS / HASH TABLES -----------------------")
print(my_hash_table.keys())

print("-----------------------  Compare O(n^2) and O(n) with HASH TABLES -----------------------")
list1 = [2,3,5]
list2 = [1,4,5]
print(item_in_common(list1, list2))
print(item_in_common_efficient(list1,list2))