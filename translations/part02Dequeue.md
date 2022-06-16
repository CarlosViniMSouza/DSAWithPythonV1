## Dequeue - Pilha no formato de Deque

Uma fila de duas extremidades, ou deque, dá suporte à adição e remoção de elementos de qualquer extremidade. As pilhas e filas mais comumente usadas são formas degeneradas de deques, onde as entradas e saídas são restritas a uma única extremidade.

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
