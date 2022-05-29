import ctypes

class DynamicArrays(object):
    # initialize (constructor)
    def __init__(self):
        self.elements = 0
        self.capacity = 1
        self.new_capacity = self.make_array(self.capacity)

    def __len__(self):
        """ Number of elements in an array"""
        return self.elements

    def __getitem__(self, index):
        """
        return index number of the elements which is located in the parameter index
        """

        if not 0 <= index <= self.elements:
            return IndexError("out of bounds")
        return self.