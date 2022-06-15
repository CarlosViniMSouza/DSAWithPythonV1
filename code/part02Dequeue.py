import collections

Dequeue = collections.deque(["Monday", "Tuersday", "Wednesday"])

Dequeue.append("Thursday")

print("\nAppended at right: ")
print(Dequeue)

Dequeue.appendleft("Sunday")

print("\nAppended at right at left is: ")
print(Dequeue)

Dequeue.pop()

print("\nDeleting from right: ")
print(Dequeue)

Dequeue.popleft()

print("\nDeleting from left: ")
print(Dequeue)
