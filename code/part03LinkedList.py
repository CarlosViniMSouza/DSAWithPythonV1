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
output:

Sunday
Monday
Tuersday
Wednesday
"""

# NOTE: This code is more complete than the previous one #

# 4. Inserting at the End
