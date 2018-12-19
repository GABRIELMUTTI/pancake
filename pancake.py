import random
import math
import time

def findIndexBiggest(list):
    indexBiggest = 0
    biggest = list[0]
    
    for i in range(1, len(list)):
        if list[i] > biggest:
            biggest = list[i]
            indexBiggest = i

    return indexBiggest

def findIndexSmallest(list):
    indexSmallest = 0
    smallest = list[0]
    
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            indexSmallest = i

    return indexSmallest

def flip(list, index):

    tmpList = list[:index + 1]
    
    for i in range(index + 1):
        list[i] = tmpList[index - i]


def isOrdered(list, indexesMap, orderFunc):
    numOrdered = 0
    isOrdered = False
    
    for i in range(len(list) - 1):
        if orderFunc(list[i], list[i + 1], indexesMap):
            if not isOrdered:
                isOrdered = True
                numOrdered += 1
            numOrdered += 1
        else:
            return numOrdered, isOrdered

    return numOrdered, isOrdered
    
        
def buildNumberIndexesMap(list):
    aList = list.copy()
    aList.sort()
    
    indexesMap = {}

    for i in range(len(aList)):
        indexesMap[aList[i]] = i

    return indexesMap

def findIndexNext(list, current, indexesMap):
    indexNext = indexesMap[current] + 1
    
    for i in range(len(list)):
        if indexNext == indexesMap[list[i]]:
            return i
    return None

def pancakeSort(list, n):
    numSorted = 0
    flips = 0 
    
    sortedList = list.copy()
    sortedList.sort()

    indexesMap = buildNumberIndexesMap(list)

    while numSorted < n:
        topNum = list[0]

        numSemiSorted, isOrderCrescent = isOrdered(list, indexesMap, crescentOrder)
        
        if numSemiSorted == n and isOrderCrescent:
            break
        
        if isOrderCrescent == True:
            flip(list, numSemiSorted - 1)
            flips += 1
            topNum = list[0]

        numSemiSorted, isOrderDecrescent = isOrdered(list, indexesMap, decrescentOrder)

        if indexesMap[list[0]] == n - numSorted - 1:
            flip(list, n - numSorted - 1)
            flips += 1
            numSorted += numSemiSorted
            topNum = list[0]

        if numSemiSorted == n:
            break

        nextIndex = findIndexNext(list[1:], topNum, indexesMap)

        flip(list, nextIndex)
        flips += 1

    return flips
        
def createRandomList(n):
    aList = list(range(n))
    random.shuffle(aList)

    return aList
        
def crescentOrder(a, b, indexesMap):
    if indexesMap[a] == indexesMap[b] - 1:
        return True
    return False

def decrescentOrder(a, b, indexesMap):
    if indexesMap[a] == indexesMap[b] + 1:
        return True
    return False



def main():
    random.seed(time.time())
    n = 1000
    flips = 0
    

    print("Creating list...")
    randomList = createRandomList(n)
    verificationList = randomList.copy()
    verificationList.sort()

    print("Pancake sort with n =", n)
    flips = pancakeSort(randomList, n)
    
    print("Sorted with", flips, "flips.")
    #print("Final:", randomList)

    wasSorted = True
    for i in range(len(verificationList)):
        if verificationList[i] != randomList[i]:
            wasSorted = False
            break

    print("Sorted?", wasSorted)
        
        
    
if __name__ == "__main__":
    main()
