class Queue:

    def __init__(self):
        self.queue = list()

    def addElement(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def removeElement(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No Elements in Queue!")

    def seeAllQueue(self):
        self.queue.reverse()
        for i in range(len(self.queue)):
            print(self.queue[i], end=" ")

    def searchElement(self, dataValue):
        if dataValue in self.queue:
            return dataValue
        else:
            return "Element not found!"

    def sizeQueue(self):
        return len(self.queue)


queue01 = Queue()

# Operation: addElement()
queue01.addElement("Mon")
queue01.addElement("Tue")
queue01.addElement("Wed")
queue01.addElement("Thu")

queue02 = Queue()

# Operation: addElement()
queue02.addElement("Jan")
queue02.addElement("Feb")
queue02.addElement("Mar")
queue02.addElement("Apr")


# Operation: removeElement()
print("\nRemoving an element of queue01:", queue01.removeElement())

print("Removing an element of queue02:", queue02.removeElement())


# Operation: sizeQueue
print("\nThe size of queue01:", queue01.sizeQueue())

print("The size of queue02:", queue02.sizeQueue())


# Operation: seeAllQueue()
print("\nThe our queue01:")
queue01.seeAllQueue()

print("\n\nThe our queue02:")
queue02.seeAllQueue()


# Operation: seachElement()
print("\n\nSearching the element in queue01:", queue01.searchElement("Sun"))

print("Searching the element in queue02:", queue02.searchElement("Feb"))
