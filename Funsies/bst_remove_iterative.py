def remove(bst, key):
    """
    Remove a key and its associated value.
    TODO: Implement this function. It must have O(log n) complexity.

    :param bst: A BinarySearchTree
    :param key: A key that can be compared with "<", ">", and "=="
    :return: The value associated with the removed key
    :raise KeyError: If the key is not in the BST
    """
    current = bst.root

    # Empty Tree
    if current is None:
        raise KeyError

    # One node and it is not the key
    if current.left is None and current.right is None and current.key != key:
        raise KeyError

    # One node and it is the key
    if current.left is None and current.right is None and current.key == key:
        temp = current.value
        bst.root = None
        bst.size -= 1
        return temp

    # If root is the key, and it has 2 kids
    if current.key == key and current.right is not None and current.left is not None:
        temp = current.value
        bst.root = successor(current)
        bst.size -= 1
        return temp

    # If root is the key, and it has one kid at the left
    if current.key == key and current.left is not None and current.right is None:
        temp = current.value
        bst.root = current.left
        bst.size -= 1
        return temp

    # If root is the key, and it has one kid at the right
    if current.key == key and current.left is None and current.right is not None:
        temp = current.value
        bst.root = current.right
        bst.size -= 1
        return temp

    while True:

        # Case 2: when remove key has no kids
        if current.left is not None and current.left.key == key and current.left.left is None and current.left.right is None:
            temp = current.left.value
            current.left = None
            bst.size -= 1
            return temp

        if current.right is not None and current.right.key == key and current.right.left is None and current.right.right is None:
            temp = current.right.value
            current.right = None
            bst.size -= 1
            return temp

        # Case 3: when remove key has one kid
        if current.left is not None and current.left.key == key and current.left.left is not None and current.left.right is None:
            temp = current.left.value
            current.left = current.left.left
            bst.size -= 1
            return temp

        if current.left is not None and current.left.key == key and current.left.left is None and current.left.right is not None:
            temp = current.left.value
            current.left = current.left.right
            bst.size -= 1
            return temp

        if current.right is not None and current.right.key == key and current.right.left is not None and current.right.right is None:
            temp = current.right.value
            current.right = current.right.left
            bst.size -= 1
            return temp

        if current.right is not None and current.right.key == key and current.right.left is None and current.right.right is not None:
            temp = current.right.value
            current.right = current.right.right
            bst.size -= 1
            return temp

        # Case 1: when removed key has both kids
        if current.left is not None and current.left.key == key and current.left.left is not None and current.left.right is not None:
            temp = current.left.value
            current.left = successor(current.left)
            bst.size -= 1
            return temp

        if current.right is not None and current.right.key == key and current.right.left is not None and current.right.right is not None:
            temp = current.right.value
            current.right = successor(current.right)
            bst.size -= 1
            return temp

        # Traversing while raising Error when deadend was met
        if key < current.key:
            if current.left is not None:
                current = current.left
            else:
                raise KeyError
        elif key > current.key:
            if current.right is not None:
                current = current.right
            else:
                raise KeyError


def successor(node):
    """Find the Smallest Thing in the Right Subtree of the tree with the remove as the root, remove that minimum from
    the right subtree and swap the root of the tree with the minimum
    :param tree: The tree with the remove as the root
    :return: The node of the root of the tree with the root swapped
    """
    current = node.right
    previous = None

    while True:
        if current.left is not None:
            previous = current
            current = current.left
        else:
            break

    min = current.key
    val = current.value

    if previous is None:
        node.right = None
        node.key = min
        node.value = val
        return node

    if previous is None and current.right is not None:
        node.right = current.right
        node.key = min
        node.value = val
        return node

    if current.right is None:
        previous.left = None
        node.key = min
        node.value = val
        return node

    if current.right is not None:
        previous.left = current.right
        node.key = min
        node.value = val
        return node