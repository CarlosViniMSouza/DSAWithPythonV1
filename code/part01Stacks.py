"""
# Code of Documentation:

stack = [3, 4, 5]

stack.append(6)  # added 6
stack.append(7)  # added 7

print(stack)
# output: [3, 4, 5, 6, 7]

print(stack.pop())  # remember: this method removed the last element on list!
# output: 7

print(stack)
# output: [3, 4, 5, 6]

stack.pop()  # dropped 6
stack.pop()  # dropped 5

print(stack)
# output: [3, 4]
"""


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
            return print("No element in the Stack")
        else:
            return self.stack.pop(-1)

    def peekStack(self):
        return self.stack[-1]

    def seeAllStack(self):
        self.stack.reverse()
        for i in range(len(self.stack)):
            print(self.stack[i])


stack01 = Stack()
stack01.addElement("Monday")
stack01.addElement("Tuersday")
stack01.addElement("Wednesday")
stack01.addElement("Thursday")

stack02 = Stack()
stack02.addElement("January")
stack02.addElement("February")
stack02.addElement("March")
stack02.addElement("April")

stack01.peekStack()
print("top of the stack01:\n", stack01.peekStack(), "\n")

stack02.peekStack()
print("top of the stack02:\n", stack02.peekStack(), "\n")

print("\nAll stack01:\n")
stack01.seeAllStack()

print("\nAll stack02:\n")
stack02.seeAllStack()

print("\nElement removed:", stack01.removeElement())
print("Element removed:", stack02.removeElement())

print("\nAll in stack01 now:\n")
stack01.seeAllStack()

print("\nAll in stack02 now:\n")
stack02.seeAllStack()

"""
output:

top of the stack01:
 Thursday 

top of the stack02:
 April 


All stack01:

Thursday
Wednesday
Tuersday
Monday

All stack02:

April
March
February
January

Element removed: Monday
Element removed: January

All in stack01 now:

Tuersday
Wednesday
Thursday

All in stack02 now:

February
March
April
"""
