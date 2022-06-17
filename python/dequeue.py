import collections


class Dequeue:

    def __init__(self):
        self.dequeue = collections.deque([])

    def addElement(self, dataValue):
        if dataValue not in self.dequeue:
            self.dequeue.append(dataValue)
            return True
        else:
            return False

    def removeElement(self):
        if len(self.dequeue) > 0:
            return self.dequeue.pop()
        else:
            return "Element cant be removed!"

    def seeAllDequeue(self):
        for i in range(len(self.dequeue)):
            print(self.dequeue[i], end=" ")

    def searchElement(self, dataValue):
        if dataValue in self.dequeue:
            return dataValue
        else:
            return "Element not found!"

    def sizeDequeue(self):
        return len(self.dequeue)

    """
    As we are working with dequeue, 
    I will add two more functions!
    """

    def addElementLeft(self, dataValue):
        if dataValue not in self.dequeue:
            self.dequeue.appendleft(dataValue)
            return True
        else:
            return False

    def removeElementLeft(self):
        if len(self.dequeue) > 0:
            return self.dequeue.popleft()
        else:
            return "Element cant be removed!"


dequeue01 = Dequeue()

# Operation: addElement()
dequeue01.addElement("01")
dequeue01.addElement("02")
dequeue01.addElement("03")
dequeue01.addElement("04")

dequeue02 = Dequeue()

# Operation: addElement()
dequeue02.addElement("01")
dequeue02.addElement("04")
dequeue02.addElement("09")
dequeue02.addElement("16")

# Operation: removeElement()
print("\nRemoving an element in dequeue01:", dequeue01.removeElement())

print("Removing an element in dequeue02:", dequeue02.removeElement())


# Operation: seeAllDequeue()
print("\nSee all elements in dequeue01:")
dequeue01.seeAllDequeue()

print("\n\nSee all elements in dequeue02:")
dequeue02.seeAllDequeue()


# Operation: searchElement()
print("\n\nSearching the element in dequeue01:", dequeue01.searchElement("10"))

print("Searching the element in dequeue02:", dequeue02.searchElement("01"))


# Operation: sizeDequeue()
print("\nThe size of dequeue01:", dequeue01.sizeDequeue())

print("The size of dequeue02:", dequeue02.sizeDequeue())


## Testing the two extras functions ##


# Operation: addElementLeft()
dequeue01.addElementLeft("-01")

dequeue02.addElementLeft("00")


# Operation: removeElementLeft()
print("\nRemoving an element (more Left) in dequeue01:",
      dequeue01.removeElementLeft())

print("Removing an element (more Left) in dequeue02:",
      dequeue02.removeElementLeft())
