#Author: Jonathan Stewart
#Project: Eve Market Scanner

import bisect

#Maintains a sorted list that does not exceed maxListSize
class ItemManager:

    def __init__(self, maxListSize):
        self.itemList = []
        self.maxListSize = maxListSize

    #PRIVATE METHODS
    #Pares down the list size to maxListSize
    #Called after insertion.
    def __truncateList(self):
        while len(self.itemList) > self.maxListSize:
            self.itemList.remove(self.itemList[len(self.itemList) - 1])

    #Performs a bisect insert
    def __binInsert(self, item):
        if len(self.itemList) < 1:
            self.itemList.insert(0, item)
            return 0
        else:
            insertionPoint = bisect.bisect_left(self.itemList, item)
            self.itemList.insert(insertionPoint, item)

            return insertionPoint

    #PUBLIC METHODS
    #Adds a list of items to the list in order.
    def addItems(self, items):
        for item in items:
            self.__binInsert(item)
        self.__truncateList()

    #Prints the complete list.
    def printList(self):
        count = 0
        for item in self.itemList:
            count += 1
            print(str(count) + '.\t', end = '')
            item.printShort()
