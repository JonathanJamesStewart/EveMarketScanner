#Author: Jonathan Stewart
#Project: Eve Market Scanner

from decimal import Decimal

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
        self.volumeCount = 1

    #Compare function.
    def __cmp__(self, other):
        return cmp(self.iskPerHour, other.iskPerHour)

    #Compare function.
    def __lt__(self, other):
        return self.iskPerHour > other.iskPerHour

    #Auto updates values that it can.
    def updateValues(self):
        #Find the average volume
        if self.volumeCount != 0:
            self.volume /= self.volumeCount

        #Calculate the isk per hour by calculating the difference
            #margin / 24
        self.iskPerHour = (self.minSell - self.maxBuy) / 24

        #Multiply the individual isk/hr by the volume sold.
        self.iskPerHour *= Decimal(self.volume)

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
        if (int(self.maxBuy) != 0 and int(self.minSell != 0)):
            temp = 1 - (float(self.maxBuy) / float(self.minSell))
            print("\t{:.0f}".format(temp * 100) + '%', end = '')
        print('\t' + self.name)
