## 5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) which was designed to have fast appends and pops from both ends. For example:

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print(queue.popleft())          # The first to arrive now leaves
# output: 'Eric'

print(queue.popleft())          # The second to arrive now leaves
# output: 'John'

print(queue)                    # Remaining queue in order of arrival
# output: deque(['Michael', 'Terry', 'Graham'])
```

## [Python - Queue - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_queue.htm)

We are familiar with queue in our day to day life as we wait for a service. The queue data structure aslo means the same where the data elements are arranged in a queue. The uniqueness of queue lies in the way items are added and removed. The items are allowed at on end but removed form the other end. So it is a *First-in-First* out method.

A queue can be implemented using python list where we can use the `.insert()` and `.pop()` methods to add and remove elements. Their is no insertion as data elements are always added at the end of the queue.

### Adding Elements

In the below example we create a queue class where we implement the *First-in-First-Out* method. We use the in-built insert method for adding data elements.

```python
class Queue:

    def __init__(self):
        self.queue = list()

    def addElement(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        else:
            return False

    def sizeQueue(self):
        return len(self.queue)


TheQueue = Queue()

TheQueue.addElement("Monday")
TheQueue.addElement("Tuersday")
TheQueue.addElement("Wednesday")
TheQueue.addElement("Thursday")

print("The size of Queue:", TheQueue.sizeQueue())
# output: The size of Queue: 4
```

### Removing Elements

In the below example we create a queue class where we insert the data and then remove the data using the in-built pop method.

```python
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

    def sizeQueue(self):
        return len(self.queue)


TheQueue = Queue()

TheQueue.addElement("Monday")
TheQueue.addElement("Tuersday")
TheQueue.addElement("Wednesday")
TheQueue.addElement("Thursday")

print("The size of Queue:", TheQueue.sizeQueue())
# output: The size of Queue: 4

print("\nRemoving an element:", TheQueue.removeElement())
# output: Removing an element: Monday

print("\nThe new size of Queue:", TheQueue.sizeQueue())
# output: The size of Queue: 3
```
