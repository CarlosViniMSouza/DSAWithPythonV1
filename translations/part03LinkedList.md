[LINK PRO ARTIGO - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)

## Definição de Lista Encadeada em Python

Uma lista encadeada é uma sequência de elementos de dados, que são conectados por meio de links. Cada elemento de dados contém uma conexão com outro elemento de dados na forma de um ponteiro. O Python não possui listas vinculadas em sua biblioteca padrão. Implementamos o conceito de listas encadeadas usando o conceito de nós como discutido no capítulo anterior.

Já vimos como criamos uma classe de nó e como percorrer os elementos de um nó. Neste capítulo vamos estudar os tipos de listas encadeadas conhecidas como listas encadeadas simples. Neste tipo de estrutura de dados existe apenas um link entre quaisquer dois elementos de dados. Criamos essa lista e criamos métodos adicionais para inserir, atualizar e remover elementos da lista.

## Lista Encadeada Individualmente

Lista vinculada simples é o tipo fundamental entre vários tipos de listas vinculadas que estão disponíveis em python. Outros tipos, como lista duplamente vinculada, lista vinculada circular, foram construídos sobre os fundamentos da lista vinculada simples. Vamos nos concentrar mais na lista vinculada individualmente

As características da lista encadeada simples são:

1. O cabeçalho do conjunto de dados sempre levará ao primeiro elemento de dados.

2. Cada nó contém dados e link para os próximos dados.

3. O link no último nó está vazio.

4. Esta lista também é conhecida como cadeia de sentido único porque os elementos de dados podem ser acessados apenas na direção, ou seja, do primeiro ao último. A navegação pelo conjunto de dados na direção reversa não é possível.

5. Qualquer elemento de dados nesta lista não pode ser acessado aleatoriamente e teremos que necessariamente percorrer sequencialmente desde o primeiro nó um por um.

Representação Fisíca:

![linked-list-img](https://cdn.educba.com/academy/wp-content/uploads/2021/05/1-3.png.webp)

## Operações de Lista Encadeada

### 1. Criação da Lista Encadeada

Uma lista encadeada é criada usando a classe de nó que estudamos no capítulo anterior. Criamos um objeto Node e criamos outra classe para usar este objeto ode. Passamos os valores apropriados através do objeto node para apontar para os próximos elementos de dados. O programa abaixo cria a lista vinculada com três elementos de dados. Na próxima seção veremos como percorrer a lista encadeada.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None

class SLinkedList:
    def __init__(self):
        self.headValue = None

list1 = SLinkedList()
list1.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Vincule o primeiro nó ao segundo nó
list1.headValue.nextValue = e2

# Vincule o segundo nó ao terceiro nó
e2.nextValue = e3
```

### 2. Percorrendo uma Lista Encadeada

Listas encadeadas simples podem ser percorridas apenas na direção direta, começando a partir do primeiro elemento de dados. Simplesmente imprimimos o valor do próximo elemento de dados atribuindo o ponteiro do próximo nó ao elemento de dados atual.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    def listprint(self):
        value = self.headValue
        while value is not None:
            print(value.data)
            value = value.nextValue


list = SinglyLinkedList()
list.headValue = Node("Monday")
e2 = Node("Tuersday")
e3 = Node("Wednesday")

# Link first Node to second node
list.headValue.nextValue = e2

# Link second Node to third node
e2.nextValue = e3

list.listprint()
```

### 3. **Inserção em uma Lista Encadeada**

Inserir elemento na lista vinculada envolve reatribuir os ponteiros dos nós existentes para o nó recém-inserido. Dependendo se o novo elemento de dados está sendo inserido no início, no meio ou no final da lista vinculada, temos os cenários abaixo.

### 3.1 Inserção no começo

Isso envolve apontar o próximo ponteiro do novo nó de dados para o cabeçalho atual da lista vinculada. Assim, o cabeçalho atual da lista vinculada se torna o segundo elemento de dados e o novo nó se torna o cabeçalho da lista vinculada.

### 3.2 Inserção no final

Isso envolve apontar o próximo ponteiro do último nó atual da lista vinculada para o novo nó de dados. Assim, o último nó atual da lista vinculada se torna o penúltimo nó de dados e o novo nó se torna o último nó da lista vinculada.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    # 2. Percorrendo a Lista Encadaeda:
    def listprint(self):
        value = self.headValue

        while value is not None:
            print(value.data)
            value = value.nextValue

    # 3. Inserção em uma Lista Encadaeda:
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Atualizando o novo nextValue existente no nó
        newNode.nextValue = self.headValue
        self.headValue = newNode

    # 4. Inserção no final
    def AtEnd(self, newData):
        newNode = Node(newData)

        if self.headValue is None:
            self.headValue = newNode
            return

        laste = self.headValue

        while laste.nextValue:
            laste = laste.nextValue
        laste.nextValue = newNode


list = SinglyLinkedList()
list.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

list.headValue.nextValue = e2
e2.nextValue = e3

list.AtEnd("Thursday")
list.listprint()
```

### 5. Inserindo entre dois nós de dados

Isso envolve alterar o ponteiro de um nó específico para apontar para o novo nó. Isso é possível passando o novo nó e o nó existente após o qual o novo nó será inserido. Assim, definimos uma classe adicional que mudará o próximo ponteiro do novo nó para o próximo ponteiro do nó do meio. Em seguida, atribua o novo nó ao próximo ponteiro do nó do meio.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    # 2. Percorrendo a Lista Encadeada:
    def listprint(self):
        value = self.headValue

        while value is not None:
            print(value.data)
            value = value.nextValue

    # 3. Inserção em uma Lista Encadeada:
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Atualizando o novo nextValue existente no nó:
        newNode.nextValue = self.headValue
        self.headValue = newNode

    # 4. Inserção no final:
    def AtEnd(self, newData):
        newNode = Node(newData)

        if self.headValue is None:
            self.headValue = newNode
            return

        laste = self.headValue

        while laste.nextValue:
            laste = laste.nextValue
        laste.nextValue = newNode

    # 5. Inserindo entre dois nós de dados
    def InBetween(self, middleNode, newData):
        if middleNode is None:
            print("The mentioned node is absent")
            return

        newNode = Node(newData)
        newNode.nextValue = middleNode.nextValue
        middleNode.nextValue = newNode


list = SinglyLinkedList()
list.headValue = Node("Monday")

e2 = Node("Tuersday")
e3 = Node("Wednesday")

list.headValue.nextValue = e2
e2.nextValue = e3

list.InBetween(list.headValue.nextValue, "Friday")
list.listprint()
```

### 6. Removendo um Item

Podemos remover um nó existente usando a chave desse nó. No programa abaixo, localizamos o nó anterior do nó que deve ser excluído. Em seguida, aponte o próximo ponteiro desse nó para o próximo nó do nó a ser excluído.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextValue = None


class SinglyLinkedList:
    def __init__(self):
        self.headValue = None

    # 2. Percorrendo uma Lista Encadeada:
    def listprint(self):
        value = self.headValue

        while value is not None:
            print(value.data)
            value = value.nextValue

    # 3. Inserção uma Lista Encadeada:
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Atualizando o novo nextValue existente no nó:
        newNode.nextValue = self.headValue
        self.headValue = newNode

    # 4. Inserção no final:
    def AtEnd(self, newData):
        newNode = Node(newData)

        if self.headValue is None:
            self.headValue = newNode
            return

        laste = self.headValue

        while laste.nextValue:
            laste = laste.nextValue
        laste.nextValue = newNode

    # 5. Inserindo entre dois nós de dados
    def InBetween(self, middleNode, newData):
        if middleNode is None:
            print("The mentioned node is absent")
            return

        newNode = Node(newData)
        newNode.nextValue = middleNode.nextValue
        middleNode.nextValue = newNode

    # 6. Removendo um item
    def RemoveNode(self, removekey):
        headVal = self.headValue

        if headVal is not None:
            if (headVal.data == removekey):
                self.headValue = headVal.nextValue
                headVal = None
                return

        while headVal is not None:
            if headVal.data == removekey:
                break

            prev = headVal
            headVal = headVal.nextValue

        if headVal == None:
            return

        prev.nextValue = headVal.nextValue
        headVal = None


list = SinglyLinkedList()
list.AtBegining("Monday")
list.AtBegining("Tuersday")
list.AtBegining("Wednesday")
list.AtBegining("Thursday")
list.RemoveNode("Tuerday")
list.listprint()

"""
output:

Thursday
Wednesday
Tuersday
Monday
"""
```
