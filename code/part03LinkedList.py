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

    # 4. Navigating data set:
    def navigateList(nL):

        if nL.startNode is None:
            print("List empty")

        print("Datas:")
        print("\n")

        node = nL.startNode

        while node is not None:
            print(node.item)
            node = node.ref


# 5. Appending Notes:
newLinkedList = LinkedListDemo()  # created a new object

newLinkedList.insertAtLast("01° - January")
newLinkedList.insertAtLast("02° - February")
newLinkedList.insertAtLast("03° - March")
newLinkedList.insertAtLast("04° - April")
newLinkedList.insertAtLast("05° - May")
newLinkedList.insertAtLast("06° - June")
newLinkedList.insertAtLast("07° - July")
newLinkedList.insertAtLast("08° - August")
newLinkedList.insertAtLast("09° - September")
newLinkedList.insertAtLast("10° - October")
newLinkedList.insertAtLast("11° - November")
newLinkedList.insertAtLast("11° - December")

newLinkedList.navigateList()

"""
This code isn't working!
I'll change for other website the linked list content.
link: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.html
"""
