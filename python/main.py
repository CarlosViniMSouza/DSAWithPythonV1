# Aqui deverá ser executado o programa que irá chamar as outras funções
import dequeue as deq
import os

# clear the terminal before of program execute the 'menu()'
os.system('clear') or None


def menu():
    resp = 1
    dequeue = deq.Dequeue()

    while resp != 0:
        print("\n\n")
        print("1 - Add Element")
        print("2 - Remove Element")
        print("3 - Visualize Estrutura")
        print("4 - Search Element")
        print("5 - Estructure Size")
        print("\n[Write '0' for finished]")

        resp = int(input("Write the operation (from 1 to 5): "))

        # clear the terminal before of show options
        os.system('clear') or None

        match(resp):

            case 1:
                valor = input("\nWrite the value for Add: ")
                dequeue.addElement(valor)

            case 2:
                print("\nLast element from estructure -> Removed")
                dequeue.removeElement()

            case 3:
                print("\nSee all estructure:")
                dequeue.seeAllDequeue()

            case 4:
                valor = input("\nWrite the value for Search: ")
                print("\nSearch Results:", dequeue.searchElement(valor))

            case 5:
                print("\nEstructure Size is:", dequeue.sizeDequeue())


if __name__ == "__main__":
    menu()
