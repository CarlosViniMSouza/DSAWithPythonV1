## 5.1.1. Usando Listas como Pilhas

Os métodos de lista tornam muito fácil usar uma lista como uma pilha, onde o último elemento adicionado é o primeiro elemento recuperado ("last-in, first-out"). Para adicionar um item ao topo da pilha, use `append()`. Para recuperar um item do topo da pilha, use `pop()` sem um índice explícito. Por exemplo:

```python
stack = [3, 4, 5]

stack.append(6)  # add 6
stack.append(7)  # add 7

print(stack)
# output: [3, 4, 5, 6, 7]

print(stack.pop())  # lembrar: esse metodo remove o ultimo elemento da lista!
# output: 7

print(stack)
# output: [3, 4, 5, 6]

stack.pop()  # tira 6
stack.pop()  # tira 5

print(stack)
# output: [3, 4]
```

## [Python - Pilha - Tutorials Point](https://www.tutorialspoint.com/python_data_structure/python_stack.htm)

No dicionário de inglês a palavra pilha significa *'organizar objetos sobre outros'*. É da mesma forma que a memória é alocada nesta estrutura de dados. Ele armazena os elementos de dados de maneira semelhante, pois vários pratos são armazenados um sobre o outro na cozinha. Assim, a estrutura de dados da pilha permite operações em uma extremidade que pode ser chamada de topo da pilha. Podemos adicionar ou remover elementos somente desta extremidade da pilha.

Em uma pilha, o elemento inserido por último na sequência sairá primeiro, pois podemos remover apenas do topo da pilha. Esse recurso é conhecido como recurso *Last In First Out(LIFO)*. As operações de adicionar e remover os elementos são conhecidas como **PUSH** e **POP**. No programa a seguir, nós a implementamos como funções **add** e **remove**. Declaramos uma lista vazia e usamos os métodos `.append()` e `.pop()` para adicionar e remover os elementos de dados.

## 1. PUSH dentro da Pilha

Vamos entender, como usar PUSH no Stack. Consulte o programa mencionado abaixo:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def addElement(self, dataValue):
        if dataValue not in self.stack:
            self.stack.append(dataValue)
            return True
        else:
            return False

    def peekStack(self):
        return self.stack[-1]

    def seeAllStack(self):
        self.stack.reverse()
        for i in range(len(self.stack)):
            print(self.stack[i])
```

## 2. POP na Pilha:

Como sabemos, podemos remover apenas o elemento de dados mais alto da pilha, implementamos um programa python que faz isso. A função remove no programa a seguir retorna o elemento mais alto. verificamos o elemento superior calculando primeiro o tamanho da pilha e, em seguida, usamos o método interno `.pop()` para descobrir o elemento superior.

```python
class Stack:
    def __init__(self):
        self.stack = []

    def addElement(self, dataValue):
        if dataValue not in self.stack:
            self.stack.append(dataValue)
            return True
        else:
            return False

    def removeElement(self):
        self.stack.reverse()
        if len(self.stack) <= 0:
            return print("No element in the Stack")
        else:
            return self.stack.pop(-1)

    def peekStack(self):
        return self.stack[-1]

    def seeAllStack(self):
        self.stack.reverse()
        for i in range(len(self.stack)):
            print(self.stack[i])
```