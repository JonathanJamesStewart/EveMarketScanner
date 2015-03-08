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

#Character vars
charName = 'Ared_Gaebril'
brokerFee = .008
salesTax = .009

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
itemList = sheetReader.getNextBatch(batchSize)

siteQuery.querySite(itemList)

for item in itemList:
    item.updateValues()

itemManager.addItems(itemList)
itemManager.printList()
