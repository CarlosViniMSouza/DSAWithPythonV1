## 5.1.2. Usando Listas como Filas

Também é possível usar uma lista como uma fila, onde o primeiro elemento adicionado é o primeiro elemento recuperado (“first-in, first-out”); no entanto, as listas não são eficientes para esta finalidade. Embora os acréscimos e pops do final da lista sejam rápidos, fazer inserções ou pops do início de uma lista é lento (porque todos os outros elementos precisam ser deslocados por um).

Para implementar uma fila, use [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) que foi projetado para ter anexos e pops rápidos de ambas as extremidades. Por exemplo:

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry chegou
queue.append("Graham")          # Graham chegou

print(queue.popleft())          # O primeiro a chegar, agora saiu
# output: 'Eric'

print(queue.popleft())          # O segundo a chegar, agora saiu
# output: 'John'

print(queue)                    # Fila restante por ordem de chegada
# output: deque(['Michael', 'Terry', 'Graham'])
```

## [Python - Fila - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_queue.htm)

Estamos familiarizados com a fila no nosso dia a dia enquanto esperamos por um serviço. A estrutura de dados da fila também significa o mesmo onde os elementos de dados são organizados em uma fila. A singularidade da fila está na forma como os itens são adicionados e removidos. Os itens são permitidos na extremidade, mas removidos da outra extremidade. Portanto, é um método *First-in-First*.

Uma fila pode ser implementada usando python list onde podemos usar os métodos `.insert()` e `.pop()` para adicionar e remover elementos. Não há inserção, pois os elementos de dados são sempre adicionados no final da fila.

### Adicionar Elementos

No exemplo abaixo, criamos uma classe queue onde implementamos o método *First-in-First-Out*. Usamos o método de inserção embutido para adicionar elementos de dados.

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

### Removendo Elementos

No exemplo abaixo, criamos uma classe de fila onde inserimos os dados e removemos os dados usando o método 'pop' embutido.

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
