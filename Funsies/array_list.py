# Implements an array list.
# CSC 202, Lab 3
# Given code, Summer '19


class PriorityQueue:
    """
    An ordered collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        if type(other) != List or self.size != other.size:
            return False

        for idx in range(self.size):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "List(%d, %r, %d)" % (self.capacity, self.array, self.size)

class Node:
    """
    A single node in a binary search tree
    NOTE: Do not alter this class.
    """

    def __init__(self, key, value, left, right):
        # The key contained in this node:
        self.key = key
        # The value associated with the key:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right

    def __eq__(self, other):
        return (type(other) == Node
                and self.value == other.value
                and self.key == other.key
                and self.left == other.left
                and self.right == other.right)

    def __repr__(self):
        return "Node(%r, %r, %r, %r)" \
               % (self.key, self.value, self.left, self.right)


def size(lst):
    """
    Count the number of elements in a list
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :return: The number of elements in the list
    """
    return lst.size


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :param idx: An index at which to get an element
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx >= lst.size or idx < 0:
        raise IndexError
    return lst.array[idx]


def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :param idx: An index at which to set an element
    :param value: A value to which to set an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx >= lst.size or idx < 0:
        raise IndexError
    lst.array[idx] = value


def enqueue(pqueue, value):
    """
    Add an element at an index, doubling capacity first if necessary.
    TODO: Implement this function. It must have O(n) complexity.

    :param pqueue: A List
    :param idx: An index at which to add an element
    :param value: A value to add as an element
    :raise IndexError: If the index is out-of-bounds
    """

    if pqueue.size == pqueue.capacity:
        pqueue.capacity *= 2
        new_array = [None] * (pqueue.capacity + 1)
        for i in range(1, pqueue.size + 1):
            new_array[i] = pqueue.array[i]
        pqueue.array = new_array

    pqueue.array[pqueue.size + 1] = value
    pqueue.size += 1

    i = pqueue.size
    while pqueue.array[i//2] < pqueue.array[i] and i//2 != 0:
        temp = pqueue.array[i//2]
        pqueue.array[i//2] = pqueue.array[i]
        pqueue.array[i] = temp





def remove(lst, idx):
    """
    Remove the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to remove an element
    :return: The removed element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx >= lst.size or idx < 0:
        raise IndexError
    remove_element = lst.array[idx]
    for i in range(idx, lst.size-1):
        lst.array[i] = lst.array[i+1]
    lst.size -= 1
    return remove_element

# lst = List()
# lst.capacity = 8
# print(lst.array)
# print(lst.array)