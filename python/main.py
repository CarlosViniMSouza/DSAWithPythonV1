# Here, the program that will call the other functions must be executed
import file as file
import os

# clear the terminal before of program execute the 'menu()'
os.system('clear') or None


def menu():
    resp = 1
    dataEstrucure = file.dataEstrucure()

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
                dataEstrucure.addElement(value)

            case 2:
                value = input("\nWrite the value for Remove: ")
                dataEstrucure.removeElement(value)

            case 3:
                print("\nSee all estructure:")
                dataEstrucure.seeAlldataEstrucure()

            case 4:
                value = input("\nWrite the value for Search: ")
                print("\nSearch Results:", dataEstrucure.searchElement(value))

            case 5:
                print("\nEstructure Size is:",
                      dataEstrucure.sizedataEstrucure())


if __name__ == "__main__":
    menu()
