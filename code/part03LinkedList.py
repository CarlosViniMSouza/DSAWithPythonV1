# Linked List Operations #

# 1. Creation of Linked list:

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValueue = None


list1 = SinglyLinkedList()
list1.headValueue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Link first Node to second node
list1.headValueue.nextValue = e2

# Link second Node to third node
e2.nextValue = e3
"""

# 2. Traversing a Linked List:

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    def listprint(self):
        value = self.headValue
        while value is not None:
            print(value.data)
            value = value.nextValue


list = SinglyLinkedList()
list.headValue = Node("Monday")
e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Link first Node to second node
list.headValue.nextValue = e2

# Link second Node to third node
e2.nextValue = e3

list.listprint()
"""

# 3. Insertion in a Linked List

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    def listprint(self):
        value = self.headValue
        while value is not None:
            print(value.data)
            value = value.nextValue

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.nextValue = self.headValue
        self.headValue = NewNode


list = SinglyLinkedList()
list.headValue = Node("Monday")
e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Link first Node to second node
list.headValue.nextValue = e2

# Link second Node to third node
e2.nextValue = e3

list.AtBegining("Sunday")
list.listprint()
"""

# 4. Inserting at the End

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    # 2. Traversing a Linked List:
    def listprint(self):
        value = self.headValue

        while value is not None:
            print(value.data)
            value = value.nextValue

    # 3. Insertion in a Linked List
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Update the new nodes next val to existing node
        newNode.nextValue = self.headValue
        self.headValue = newNode

    # 4. Inserting at the End
    def AtEnd(self, newData):
        newNode = Node(newData)

        if self.headValue is None:
            self.headValue = newNode
            return

        laste = self.headValue

        while laste.nextValue:
            laste = laste.nextValue
        laste.nextValue = newNode


list = SinglyLinkedList()
list.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

list.headValue.nextValue = e2
e2.nextValue = e3

list.AtEnd("Thursday")
list.listprint()
"""

# 5. Inserting in between two Data Nodes


class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    # 2. Traversing a Linked List:
    def listprint(self):
        value = self.headValue

        while value is not None:
            print(value.data)
            value = value.nextValue

    # 3. Insertion in a Linked List
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Update the new nodes next val to existing node
        newNode.nextValue = self.headValue
        self.headValue = newNode

    # 4. Inserting at the End
    def AtEnd(self, newData):
        newNode = Node(newData)

        if self.headValue is None:
            self.headValue = newNode
            return

        laste = self.headValue

        while laste.nextValue:
            laste = laste.nextValue
        laste.nextValue = newNode

    # 5. Inserting in between two Data Nodes
    def InBetween(self, middleNode, newData):
        if middleNode is None:
            print("The mentioned node is absent")
            return

        newNode = Node(newData)
        newNode.nextValue = middleNode.nextValue
        middleNode.nextValue = newNode


list = SinglyLinkedList()
list.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

list.headValue.nextValue = e2
e2.nextValue = e3

list.InBetween(list.headValue.nextValue, "Friday")
list.listprint()

"""
output:

Monday
Tuersday
Friday
Wednesday
"""

# NOTE: This code is more complete than the previous one #
