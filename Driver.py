#Author: Jonathan Stewart
#Project: Eve Market Scanner

from SheetReader import *
from ItemManager import *
from Query import *

#VARIABLES
#Book path
bookPath = 'invTypes.xls'
sheetNumber = 0

#System vars for the main trading hub
regionID = 10000002
systemID = 30000142

#Boundary conditions
maxPrice = 50000000
maxListSize = 500
batchSize = 100
numDays = 10
highMargin = 2
lowMargin = .05

#Character vars
charName = 'Ared_Gaebril'
brokerFee = .008
salesTax = .009

#Misc vars
queryCount = 0

#DRIVER
#Init utility classes
sheetReader = SheetReader()
itemManager = ItemManager(maxListSize)
siteQuery = Query()

#Init parameters
sheetReader.setBook(bookPath)
sheetReader.setSheet(sheetNumber)

siteQuery.setSystemID(systemID)
siteQuery.setRegionID(regionID)
siteQuery.setCharName(charName)
siteQuery.setNumDays(numDays)

#***TESTING***
while sheetReader.hasMoreRows():
    itemList = sheetReader.getNextBatch(batchSize)

    siteQuery.querySite(itemList)
    queryCount += 1
    print('Queries made: ' + str(queryCount))

    for item in itemList:
        #Adjust sell and buy for fees and taxes
        item.minSell = Decimal(item.minSell) - (Decimal(item.minSell) * Decimal(brokerFee)) - (Decimal(item.minSell) * Decimal(salesTax))
        item.maxBuy = Decimal(item.maxBuy) + (Decimal(item.maxBuy) * Decimal(brokerFee))

        item.updateValues()

        #Remove it if the market is unreasonable
        if (float(item.maxBuy) != 0):
            if (float(item.minSell) / float(item.maxBuy)) > highMargin:
                try:
                    itemList.remove(item)
                except:
                    pass
        #Remove it if the item is too expensive
        if (item.maxBuy > maxPrice):
            try:
                itemList.remove(item)
            except:
                pass
        #Remove if the profit margin is too small.
        if (float(item.minSell) != 0):
            if (float(item.maxBuy) / float(item.minSell)) > (1 - lowMargin):
                try:
                    itemList.remove(item)
                except:
                    pass
##        else:
##            self.removeItem(itemList, item)

        #Remove if it is a blueprint
        if 'Blueprint' in item.name:
            try:
                itemList.remove(item)
            except:
                pass

    itemManager.addItems(itemList)

itemManager.printList()    
