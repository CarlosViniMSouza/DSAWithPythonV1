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
            self.queue.append(data)
            return True
        return False

    def removeElement(self):
        try:
            if len(self.queue) > 0:
                return self.queue.pop()
        except:
            return ("No Elements in Queue!")

    def showQueue(self):
        try:
            if len(self.queue) > 0:
                print(self.queue)
        except:
            return ("Queue Empty")

    def sizeQueue(self):
        return len(self.queue)


TheQueue = Queue()

TheQueue.addElement("Monday")
TheQueue.addElement("Tuersday")
TheQueue.addElement("Wednesday")
TheQueue.addElement("Thursday")

print("The size of Queue:", TheQueue.sizeQueue())
# output: The size of Queue: 4

print("\nThe Queue maked:")
TheQueue.showQueue()
# output: ['Thursday', 'Wednesday', 'Tuersday', 'Monday']

print("\nRemoving an element:", TheQueue.removeElement())
# output: Removing an element: Monday

print("\nThe new size of Queue:", TheQueue.sizeQueue())
# output: The size of Queue: 3

print("\nThe new Queue maked:")
TheQueue.showQueue()
# output: ['Thursday', 'Wednesday', 'Tuersday']
