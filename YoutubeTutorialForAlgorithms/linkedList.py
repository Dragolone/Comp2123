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
        while current:
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
                nodes.append("[Tail: %s]" % current.data)
            current = current.nextNode
        return '->'.join(nodes)

l1 = LinkedList()
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
#
# l1.head = n1
# n1.nextNode = n2
# n2.nextNode = n3
# l1.tail = n3
#
# l1.add("begin")

l1.add(1)
l1.add(2)
l1.add(3)
print(l1.__repr__())
print(l1.size())
