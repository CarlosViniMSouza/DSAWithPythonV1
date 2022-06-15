"""
from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives

print(queue.popleft())  # The first to arrive now leaves
# output: 'Eric'

print(queue.popleft())  # The second to arrive now leaves
# output: 'John'

print(queue)            # Remaining queue in order of arrival
# output: deque(['Michael', 'Terry', 'Graham'])"""


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
