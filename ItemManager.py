#Author: Jonathan Stewart
#Project: Eve Market Scanner

#Maintains a sorted list that does not exceed maxListSize
class ItemManager:

    def __init__(self, maxListSize):
        self.itemList = []
        self.maxListSize = maxListSize

    def addItems(self, items):
        self.itemList.append(items)
        truncateList()

    def truncateList(self):
        while len(self.itemList) > maxListSize:
            self.itemList.remove(self.itemList[len(self.itemList) - 1])
