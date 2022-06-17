Já vimos Lista Encadeada no capítulo anterior em que só é possível viajar para a frente. Neste capítulo vemos outro tipo de lista encadeada na qual é possível viajar tanto para frente quanto para trás. Essa lista encadeada é chamada de lista duplamente encadeada. A seguir estão os recursos da lista duplamente vinculada.

1. Lista duplamente vinculada contém um elemento de link chamado first e last.

2. Cada link carrega um(s) campo(s) de dados e dois campos de link chamados next e prev.

3. Cada link é vinculado ao seu próximo link usando seu próximo link.

4. Cada link é vinculado ao seu link anterior usando seu link anterior.

5. O último link carrega um link como nulo para marcar o fim da lista.

## Criando lista duplamente encadeada

Criamos uma lista duplamente vinculada usando a classe `Node`. Agora, usamos a mesma abordagem usada na Lista Encadeada Simples, mas os ponteiros `head` e `next` serão usados para a atribuição adequada para criar dois links em cada um dos nós, além dos dados presentes no nó.

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

## Inserindo em uma lista duplamente vinculada

Aqui, veremos como inserir um nó na Double Link List usando o programa a seguir. O programa usa um método chamado `insert` que insere o novo nó na terceira posição do início da lista duplamente encadeada.

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

## Anexando a uma lista duplamente vinculada

Anexar a uma lista duplamente vinculada adicionará o elemento no final.

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

    def append(self, newVal):
        newNode = Node(newVal)
        newNode.nextValue = None

        if self.head is None:
            newNode.preValue = None
            self.head = newNode
            return

        last = self.head

        while last.nextValue is not None:
            last = last.nextValue

        last.nextValue = newNode
        newNode.preValue = last
        return

    # Print the Doubly Linked list
    def listprint(self, node):
        while node is not None:
            print(node.dataValue, end=" -> "),
            node = node.nextValue


lla = doubly_linked_list()
lla.push(12)
lla.append(9)
lla.push(6)
lla.push(24)
lla.append(30)
lla.insert(lla.head.nextValue, 13)
lla.listprint(lla.head)
```
