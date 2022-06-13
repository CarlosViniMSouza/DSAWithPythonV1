## 5.1.1. Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use `append()`. To retrieve an item from the top of the stack, use `pop()` without an explicit index. For example:

```python
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
```

## [Python - Stack - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_stack.htm)

In the english dictionary the word stack means *'arranging objects on over another'*. It is the same way memory is allocated in this data structure. It stores the data elements in a similar fashion as a bunch of plates are stored one above another in the kitchen. So stack data strcuture allows operations at one end wich can be called top of the stack.We can add elements or remove elements only form this en dof the stack.

In a stack the element insreted last in sequence will come out first as we can remove only from the top of the stack. Such feature is known as *Last in First Out(LIFO)* feature. The operations of adding and removing the elements is known as **PUSH** and **POP**. In the following program we implement it as **add** and **remove** functions. We declare an empty list and use the `.append()` and `.pop()` methods to add and remove the data elements.

## 1. PUSH into a Stack

Let us understand, how to use PUSH in Stack. Refer the program mentioned program below:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def addElement(self, dataValue):
        if dataValue not in self.stack:
            self.stack.append(dataValue)
            return True
        else:
            return False

    def peekStack(self):
        return self.stack[-1]

    def seeAllStack(self):
        self.stack.reverse()
        for i in range(len(self.stack)):
            print(self.stack[i])
```

## 2. POP from a Stack

As we know we can remove only the top most data element from the stack, we implement a python program which does that. The remove function in the following program returns the top most element. we check the top element by calculating the size of the stack first and then use the in-built `.pop()` method to find out the top most element.

```python
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
```