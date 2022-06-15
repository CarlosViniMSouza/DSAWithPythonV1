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

"""
output:

1. The original dequeue: deque(['Monday', 'Tuersday', 'Wednesday'])

2. Appended at right: deque(['Monday', 'Tuersday', 'Wednesday', 'Thursday'])

3. Appended at right at left is: deque(['Sunday', 'Monday', 'Tuersday', 'Wednesday', 'Thursday'])

4. Deleting from right: deque(['Sunday', 'Monday', 'Tuersday', 'Wednesday'])

5. Deleting from left: deque(['Monday', 'Tuersday', 'Wednesday'])
"""
