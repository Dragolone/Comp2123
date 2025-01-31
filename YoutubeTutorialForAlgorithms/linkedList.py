class Node:
    """
    An object for sorting a single node of a linked list.
    Models two attributes: data and the link to the next node in the list
    """
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    """
    Singly linked list class
    """
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.nextNode
        return count

    def add(self, data):
        """
        Adds a new node at the head of the linked list.
        Updates the tail if the list was previously empty.
        :param data: The value to be stored in the new node.
        """
        newNode = Node(data)  # Create a new node with the given data
        newNode.nextNode = self.head  # Link the new node to the current head
        self.head = newNode  # Update head to point to the new node

        if self.tail is None:  # If the list was empty, update tail to the new node
            self.tail = newNode

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        Takes O(n) time complexity where n is the size of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[Next: %s]" % current.data)
            current = current.nextNode
        return '->'.join(nodes)

    def search(self, key):
        """
        Searches for the first node whose data is equal to the given key.
        :param key:
        :return:Node or None
        O(n) time complexity where n is the size of the linked list.
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.nextNode
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            newNode = Node(data)
            position = index - 1
            current = self.head

            while position > 0 and current is not None:
                current = current.nextNode
                position -= 1
            if current is None:
                raise IndexError("Index out of range")
            newNode.nextNode = current.nextNode
            current.nextNode = newNode

            if newNode.nextNode is None:
                self.tail = newNode

    def remove_index(self, index):
        if index >= self.size() or index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.nextNode
            if self.head is None:
                self.tail = None

        if index > 0:
            current = self.head
            position = index - 1
            while position > 0 and current is not None:
                current = current.nextNode
                position -= 1

            current.nextNode = current.nextNode.nextNode

            # If we deleted the last node, update `tail`
            if current.nextNode is None:
                self.tail = current
    def remove_key(self, key):
        current = self.head



"""
1 2 3 4 5 6 7 8 9
index = 2
position = index + 1
"""

l1 = LinkedList()
# # n1 = Node(1)
# # n2 = Node(2)
# # n3 = Node(3)
# #
# # l1.head = n1
# # n1.nextNode = n2
# # n2.nextNode = n3
# # l1.tail = n3
# #
# # l1.add("begin")
l1.add(1)
l1.add(2)
l1.add(3)
l1.insert(200, 3)
l1.remove(2)

print(l1.__repr__())
print(l1.size())
