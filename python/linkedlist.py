# Here, the things is a little diferent, compared to stacks, queues and decks ...


class LinkedList:

    def __init__(self, data=None):
        self.headData = None
        self.nextData = None
        self.data = data

    def addElementAtBeg(self, newData):
        node = LinkedList(newData)

        # Update values on List
        node.nextData = self.headData
        self.headData = node

    def addElementAtEnd(self, newData):
        node = LinkedList(newData)

        if self.headData is None:
            self.headData = node
            return 0

        last = self.headData

        while last.nextData is not None:
            last = last.nextData

        last.nextData = node

    def addElementAtBet(self, middleData, newData):
        if middleData is None:
            return "This node were not found"

        node = LinkedList(newData)
        node.nextData = middleData
        middleData = node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list.
    def removeElement(self, removeData):

        # Store head node
        dataDel = self.headData

        # If head node itself holds the key to be deleted
        if dataDel is not None:
            if dataDel.data == removeData:
                self.headData = dataDel.nextData
                dataDel = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'.
        while dataDel is not None:
            if dataDel.data == removeData:
                break

            dataPrev = dataDel
            dataDel = dataDel.nextData

        # if key was not present in linked list
        if dataDel == None:
            return

        # Unlink the node from linked list
        dataPrev.nextData = dataDel.nextData
        dataDel = None

    # Utility function to print the linked LinkedList
    def seeAllLinkedList(self):
        value = self.headData

        while value is not None:
            print(value.data, end=" ")
            value = value.nextData

    # This Function checks whether the value
    # 'dataValue' present in the linked list
    def searchElement(self, dataValue):

        # Initialize current to head
        value = self.headData

        # Loop till current not equal to None
        while value != None:

            if value.data == dataValue:
                # Data found
                return dataValue

            value = value.nextData

        # Data Not Found
        return "Element not found!"

    def sizeLinkedList(self):
        value = self.headData
        cont = 0

        while value is not None:
            cont += 1
            value = value.nextData

        return cont


linkedList = LinkedList()

# Operation: addElement()
linkedList.addElementAtBeg("sun")
linkedList.addElementAtBeg("mon")
linkedList.addElementAtBeg("tue")
linkedList.addElementAtEnd("wed")
linkedList.addElementAtEnd("thu")
linkedList.addElementAtEnd("fri")
# linkedList.addElementAtBet(linkedList.headData, "sat")


# Operation: searchElement()
print("\nSearching the element in linked List:",
      linkedList.searchElement("mon"))

print("Searching the element in linked List:",
      linkedList.searchElement("dew"))


# Operation: seeAllLinkedList()
print("\nThe Linked List Elements:")
linkedList.seeAllLinkedList()


# Operation: removeElement()
print("\n\nRemoving an element ...")
linkedList.removeElement("wed")


# Operation: seeAllLinkedList()
print("\nThe Linked List Elements:")
linkedList.seeAllLinkedList()


# Operation: sizeLinkedList()
print("\n\nThe size of linked list:", linkedList.sizeLinkedList())
