class Stack:
    def __init__(self):
        self.stack = []

    def addElement(self, dataValue):
        if dataValue not in self.stack:
            self.stack.append(dataValue)
            return True
        else:
            return False

    def removeElement(self):
        self.stack.reverse()
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop(-1)

    def seeAllStack(self):
        self.stack.reverse()
        for i in range(len(self.stack)):
            print(self.stack[i])

    def searchElement(self, dataValue):
        if dataValue in self.stack:
            return dataValue
        else:
            return "Element not found!"

    def sizeStack(self):
        return len(self.stack)


stack01 = Stack()

# Creating the stack01
stack01.addElement("Monday")
stack01.addElement("Tuersday")
stack01.addElement("Thursday")
stack01.addElement("Wednesday")


stack02 = Stack()

# Creating the stack02
stack02.addElement("March")
stack02.addElement("April")
stack02.addElement("January")
stack02.addElement("February")


# Operation: seeAllStack()
print("\nAll in stack01:\n")
stack01.seeAllStack()

print("\nAll in stack02:\n")
stack02.seeAllStack()


# Operation: removeElement()
print("\nElement removed:", stack01.removeElement())

print("\nElement removed:", stack02.removeElement())


# Operation: seeAllStack()
print("\nAll in stack01 now:\n")
stack01.seeAllStack()

print("\nAll in stack02 now:\n")
stack02.seeAllStack()


# Operation: searchElement()
print("\nSearching the element:", stack01.searchElement("Wedneday"))

print("\nSearching the element:", stack02.searchElement("February"))


# Operation: sizeStack():
print("\nThe size of stack01:", stack01.sizeStack())

print("\nThe size of stack02:", stack02.sizeStack())
