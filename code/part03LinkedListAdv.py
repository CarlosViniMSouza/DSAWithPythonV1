class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.nextValue = None
        self.preValue = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    # Adding data elements
    def push(self, newVal):
        newNode = Node(newVal)
        newNode.nextValue = self.head

        if self.head is not None:
            self.head.preValue = newNode
        self.head = newNode

    # Define the insert method to insert the element
    def insert(self, preNode, newVal):
        if preNode is None:
            return

        newNode = Node(newVal)
        newNode.nextValue = preNode.nextValue
        preNode.nextValue = newNode
        newNode.preValue = preNode

        if newNode.nextValue is not None:
            newNode.nextValue.prev = newNode

# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.dataValue),
            last = node  # 'last' is unnecessary -> apparently ...
            node = node.nextValue


lla = doubly_linked_list()
lla.push(12)
lla.push(8)
lla.push(62)
lla.insert(lla.head.nextValue, 13)
lla.listprint(lla.head)

"""
output:

62
8
13
12
"""
