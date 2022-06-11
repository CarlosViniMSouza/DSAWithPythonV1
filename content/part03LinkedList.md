[LINK FOR ARTICLE - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)

## Definition of Linked List in Python

A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes as discussed in the previous chapter.

We have already seen how we create a node class and how to traverse the elements of a node.In this chapter we are going to study the types of linked lists known as singly linked lists. In this type of data structure there is only one link between any two data elements. We create such a list and create additional methods to insert, update and remove elements from the list.

## Singly Linked List

Singly-linked list is the fundamental type among various types of linked lists that are available in python. Other types such as Doubly linked list, Circular linked list were built over the basics of singly linked list. Let’s focus more on singly linked list

Features of singly linked list are:

1. Header of dataset will always lead to first data element.

2. Each node contains data and link to next data.

3. The link in the last node is empty.

4. This list is also known as one way chain because the data elements can be accessed in only direction i.e. first to last. Navigation through dataset in reverse direction is not possible.

5. Any data element in this list cannot be accessed randomly and we will have to necessarily traverse sequentially from the first node one by one.

Pictorial Representation:

![linked-list-img](https://cdn.educba.com/academy/wp-content/uploads/2021/05/1-3.png.webp)

## Linked List Operations

### 1. Creation of Linked list

A linked list is created by using the node class we studied in the last chapter. We create a Node object and create another class to use this ode object. We pass the appropriate values through the node object to point the to the next data elements. The below program creates the linked list with three data elements. In the next section we will see how to traverse the linked list.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None

class SLinkedList:
    def __init__(self):
        self.headValue = None

list1 = SLinkedList()
list1.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Link first Node to second node
list1.headValue.nextValue = e2

# Link second Node to third node
e2.nextValue = e3
```

### 2. Traversing a Linked List

Singly linked lists can be traversed in only forward direction starting form the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element.

```python
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
```

### 3. **Insertion in a Linked List**

Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted node. Depending on whether the new data element is getting inserted at the beginning or at the middle or at the end of the linked list, we have the below scenarios.

### Inserting at the Beginning

This involves pointing the next pointer of the new data node to the current head of the linked list. So the current head of the linked list becomes the second data element and the new node becomes the head of the linked list.

### 4. Inserting at the End

This involves pointing the next pointer of the the current last node of the linked list to the new data node. So the current last node of the linked list becomes the second last data node and the new node becomes the last node of the linked list.

```python
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
```

### 5. Inserting in between two Data Nodes

This involves changing the pointer of a specific node to point to the new node. That is possible by passing in both the new node and the existing node after which the new node will be inserted. So we define an additional class which will change the next pointer of the new node to the next pointer of middle node. Then assign the new node to next pointer of the middle node.

```python
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
```

### 6. Removing an Item

We can remove an existing node using the key for that node. In the below program we locate the previous node of the node which is to be deleted.Then, point the next pointer of this node to the next node of the node to be deleted.
