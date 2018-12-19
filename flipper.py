import os
from pancake import flip
from pancake import createRandomList

def printList(list):
    print(' ', end = '')
    for i in range(len(list)):
        print(i + 1, '-', end = '-')
        if i < 9: print('-', end = '')
        
    print("")
    print('[', end = '')
    for i, val in enumerate(list):
        print(val, end = '')
        if i != len(list) - 1:
            print(',', end = '  ')
        if val < 10: print(' ', end = '')
    print(']', end = '')
    print('\n')

    

            
def flipper(list):
    originalList = list.copy()
    flips = 0
    lastIndex = 0

    userInput = ''
    while True:
   
        printList(list)
        userInput = input("Index to flip: ")

        if userInput == 'x':
            break
        elif userInput == 'r':
            list = originalList.copy()
            flips = 0
            print("Reseted.\n")
        elif userInput == 'f':
            print("Flips:", flips, "\n")
        elif userInput == 'u':
            flip(list, lastIndex)
            flips -= 1
        elif int(userInput) > len(list):
            print("Index out of range.\n")
        else:
            flip(list, int(userInput) - 1)
            lastIndex = int(userInput) - 1
            flips += 1
    

def buildList():
    ENTER = ''
    list = []

    userInput = input("Enter the list numbers:\n")
    while userInput != ENTER:
        list.append(int(userInput))
        userInput = input()

    return list


def chooseList():
    print("1 - [10, 3, 6, 9, 14, 12, 1, 15, 8, 16, 5, 11, 7, 13, 2, 4]")
    print("1 - [23, 10, 25, 3, 6, 24, 18, 9, 14, 22, 12, 26, 17, 1, 15, 19, 8, 21, 16, 5, 20, 11, 7, 13, 27, 2, 4]")

    list = []
    userInput = input("> ")
    if userInput == '1':
        return [10, 3, 6, 9, 14, 12, 1, 15, 8, 16, 5, 11, 7, 13, 2, 4]
    elif userInput == '2':
        return [23, 10, 25, 3, 6, 24, 18, 9, 14, 22, 12, 26, 17, 1, 15, 19, 8, 21, 16, 5, 20, 11, 7, 13, 27, 2, 4]

    
def randomList():
    length = input("Enter list length: ")
    numRange = input("Enter num range: ")

    return createRandomList(int(length), int(numRange))
    
    
def main():

    print("1 - Build list.")
    print("2 - Select List")
    print("3 - Random List")
    userInput = input("> ")

    list = []
    if userInput == '1':
        list = buildList()
    elif userInput == '2':
        list = chooseList()
    elif userInput == '3':
        list = randomList()

    flipper(list)

if __name__ == "__main__":
    main()
