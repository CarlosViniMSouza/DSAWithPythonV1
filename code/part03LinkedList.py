# 6. Removing an item:

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

    # 6. Removing an item
    def RemoveNode(self, removekey):
        headVal = self.headValue

        if headVal is not None:
            if headVal.data == removekey:
                self.headValue = headVal.nextValue
                headVal = None
                return

        while headVal is not None:
            if headVal.data == removekey:
                break

            prev = headVal
            headVal = headVal.nextValue

        if headVal == None:
            return

        prev.nextValue = headVal.nextValue
        headVal = None


list = SinglyLinkedList()
list.AtBegining("Monday")
list.AtBegining("Tuersday")
list.AtBegining("Wednesday")
list.AtBegining("Thursday")

list.RemoveNode("Tuerday")

list.listprint()

"""
output:

Thursday
Wednesday
Tuersday
Monday
"""

# NOTE: This code is more complete than the previous one #
