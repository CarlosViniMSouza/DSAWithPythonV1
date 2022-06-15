## Dequeue - Stack in deque format 

A double-ended queue, or deque, supports adding and removing elements from either end. The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.

```python
import collections

Dequeue = collections.deque(["Monday", "Tuersday", "Wednesday"])

print(f"\n1. The original dequeue: {Dequeue}")

Dequeue.append("Thursday")

print(f"\n2. Appended at right: {Dequeue}")

Dequeue.appendleft("Sunday")

print(f"\n3. Appended at right at left is: {Dequeue}")

Dequeue.pop()

print(f"\n4. Deleting from right: {Dequeue}")

Dequeue.popleft()

print(f"\n5. Deleting from left: {Dequeue}")
```
