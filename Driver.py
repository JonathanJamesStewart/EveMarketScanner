#Author: Jonathan Stewart
#Project: Eve Market Scanner

from SheetReader import *

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

#Character vars
charName = 'Ared_Gaebril'
brokerFee = .008
salesTax = .009

#DRIVER
#Init utility classes
sheetReader = SheetReader()

#Init parameters
sheetReader.setBook(bookPath)
sheetReader.setSheet(sheetNumber)

#***TESTING***
for i in range(1, 3):
    count = 0
    
    itemList = sheetReader.getNextBatch(batchSize)
    for item in itemList:
        print(count, end="")
        item.printShort()
        count += 1
        
