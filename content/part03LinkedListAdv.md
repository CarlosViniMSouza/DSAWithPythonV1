We have already seen Linked List in earlier chapter in which it is possible only to travel forward. In this chapter we see another type of linked list in which it is possible to travel both forward and backward. Such a linked list is called Doubly Linked List. Following is the features of doubly linked list.

1. Doubly Linked List contains a link element called first and last.

2. Each link carries a data field(s) and two link fields called next and prev.

3. Each link is linked with its next link using its next link.

4. Each link is linked with its previous link using its previous link.

5. The last link carries a link as null to mark the end of the list.

## Creating Doubly linked list

We create a Doubly Linked list by using the Node class. Now we use the same approach as used in the Singly Linked List but the head and next pointers will be used for proper assignation to create two links in each of the nodes in addition to the data present in the node.

```python
class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.nextValue = None
        self.preValue = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

# Adding data elements
    def push(self, newVal):
        NewNode = Node(newVal)
        NewNode.nextValue = self.head
        if self.head is not None:
            self.head.preValue = NewNode
        self.head = NewNode

# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.dataValue),
            last = node  # 'last' is unnecessary -> apparently ...
            node = node.nextValue


lla = doubly_linked_list()
lla.push(12)
lla.push(8)
lla.push(62)
lla.listprint(lla.head)
```

## Inserting into Doubly Linked List

Here, we are going to see how to insert a node to the Doubly Link List using the following program. The program uses a method named insert which inserts the new node at the third position from the head of the doubly linked list.

```python
class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.nextValue = None
        self.preValue = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    # Adding data elements
    def push(self, newVal):
        newNode = Node(newVal)
        newNode.nextValue = self.head

        if self.head is not None:
            self.head.preValue = newNode
        self.head = newNode

    # Define the insert method to insert the element
    def insert(self, preNode, newVal):
        if preNode is None:
            return

        newNode = Node(newVal)
        newNode.nextValue = preNode.nextValue
        preNode.nextValue = newNode
        newNode.preValue = preNode

        if newNode.nextValue is not None:
            newNode.nextValue.prev = newNode

# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.dataValue),
            last = node  # 'last' is unnecessary -> apparently ...
            node = node.nextValue


lla = doubly_linked_list()
lla.push(12)
lla.push(8)
lla.push(62)
lla.insert(lla.head.nextValue, 13)
lla.listprint(lla.head)
```

## Appending to a Doubly linked list

Appending to a doubly linked list will add the element at the end.

```python

```
