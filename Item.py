#Author: Jonathan Stewart
#Project: Eve Market Scanner

#Simple class for storage of item information.
class Item:

    #Init
    def __init__(self, name, itemID):
        self.maxBuy = 0
        self.minSell = 0
        self.name = name
        self.itemID = itemID
        self.iskPerHour = 0
        self.volume = 0
        self.volumeCount = 0

    def __cmp__(self, other):
        return cmp(self.iskPerHour, other.iskPerHour)

    def __lt__(self, other):
        return self.iskPerHour < other.iskPerHour

    #Prints full description. Formatting should be obvious.
    def printItem(self):
        print('Name: ' + self.name, end = '')
        print(' ID: ' + str(self.itemID), end = '')
        print(' minBuy: ' + "{:,.2f}".format(self.maxBuy), end = '')
        print(' maxSell: ' + "{:,.2f}".format(self.minSell), end = '')
        print(' Volume: ' + "{:,.0f}".format(self.volume), end = '')
        print(' iskPerHour: ' + "{:,.0f}".format(self.iskPerHour))

    #Prints description of self in the following format:
    #iskPerHour \t %profit \t name
    def printShort(self):
        print("{:,.0f}".format(self.iskPerHour), end = '')
        if (int(self.maxBuy) != 0):
            temp = 1 - (float(self.maxBuy) / float(self.minSell))
            print("\t{:.4f}".format(temp), end = '')
        print('\t' + self.name)
