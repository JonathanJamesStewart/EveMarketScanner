#Author: Jonathan Stewart
#Project: Eve Market Scanner

import bisect

#Maintains a sorted list that does not exceed maxListSize
class ItemManager:

    def __init__(self, maxListSize):
        self.itemList = []
        self.maxListSize = maxListSize

    #PRIVATE METHODS
    def __truncateList(self):
        while len(self.itemList) > self.maxListSize:
            self.itemList.remove(self.itemList[len(self.itemList) - 1])

    def __binInsert(self, item):
        if len(self.itemList) < 1:
            self.itemList.insert(0, item)
            return 0
        else:
            insertionPoint = bisect.bisect_left(self.itemList, item)
            self.itemList.insert(insertionPoint, item)

            return insertionPoint

    #PUBLIC METHODS
    def addItems(self, items):
        for item in items:
            self.__binInsert(item)
        self.itemList.append(items)
        self.__truncateList()

    def printList(self):
        for item in self.itemList:
            item.printShort()
