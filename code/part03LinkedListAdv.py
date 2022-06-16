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
        NewNode = Node(newVal)
        NewNode.nextValue = self.head
        if self.head is not None:
            self.head.preValue = NewNode
        self.head = NewNode

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
lla.listprint(lla.head)
