# Aqui deverá ser executado o programa que irá chamar as outras funções
import linkedlist as ll
import os

# clear the terminal before of program execute the 'menu()'
os.system('clear') or None


def menu():
    resp = 1
    linkedList = ll.LinkedList()

    while resp != 0:
        print("\n\n")
        print("1 - Add Element")
        print("2 - Remove Element")
        print("3 - View Estructure")
        print("4 - Search Element")
        print("5 - Estructure Size")
        print("\n[Write '0' for finished]")

        resp = int(input("Write the operation (from 1 to 5): "))

        # clear the terminal before of show options
        os.system('clear') or None

        match(resp):

            case 1:
                value = input("\nWrite the value for Add: ")
                linkedList.addElementAtBeg(value)

            case 2:
                value = input("\nWrite the value for Remove: ")
                linkedList.removeElement(value)

            case 3:
                print("\nSee all estructure:")
                linkedList.seeAllLinkedList()

            case 4:
                value = input("\nWrite the value for Search: ")
                print("\nSearch Results:", linkedList.searchElement(value))

            case 5:
                print("\nEstructure Size is:", linkedList.sizeLinkedList())


if __name__ == "__main__":
    menu()
