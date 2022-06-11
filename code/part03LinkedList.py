# Linked List Operations #


# 1. Node Creation:
class Node:
    def __init__(dataNode, data):
        dataNode.item = data  # Node created with data
        dataNode.ref = None  # Link is pointing to null


# 2. Linked List Creation:
class LinkedListDemo:
    def __init__(lld):
        lld.startNode = None
        # our first node

    # 3. Insert at 'The End':
    def insertAtLast(iAL, data):
        newNode = Node(data)       # move data

        if iAL.startNode is None:  # empty set
            iAL.startNode = newNode

        node = iAL.startNode

        while node.ref is not None:
            node = node.ref
            node.ref = newNode  # new node is the last

        return node
