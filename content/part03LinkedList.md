[LINK FOR ARTICLE - EDUCBA](https://www.educba.com/linked-list-in-python/)

## Definition of Linked List in Python

Linked list in Python provides a logical connection between data elements that are stored in memory in different locations physically. Data elements are stored in nodes along with reference links to the next immediate data element. Logical sequencing of data is achieved in Python through these links in data nodes and the entire gamut of data can be accessed sequentially using these links by navigating from the first data element to the next and so on.

Linked list in Python removes the hassle of pre-defining the memory blocks, provides flexibility to scale up data dynamically, simplifies the data operations, and ensures optimum usage of memory.

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

### 1. Node creation

A program class to create a node should be defined as a first step in the python program and the data objects can be created as when required.

```python
class Node:
  def __init__(data_node, data):
    data_node.item = data # Node created with data
    data_node.ref = None  # Link is pointing to null
```

### 2. Linked List Creation

Another program class to create linked list with initial values should be defined in the program as next step. This class would contain steps for subsequent operations like `Inserting`, `Delete`, `Traverse` (Navigation).

```python
class LinkedListDemo:
    def __init__(lld):
        lld.start_node = None
        # our first node
```

### 3. Initial Data Loading (Insert at The End)

Ideally the initial loading can happen from the end of the empty data set. While inserting a new data, If the dataset is empty make the new node as the first and last node and exit. If data is present in the dataset then navigate to end, make the current last node as last but one node. New node will be the last.

```python
def insertAtLast(iAL, data):
    newNode = Node(data)       # move data

    if iAL.startNode is None:  # empty set
        iAL.startNode = newNode

    node = iAL.startNode

    while node.ref is not None:
        node = node.ref
        node.ref = newNode  # new node is the last

    return node
```
