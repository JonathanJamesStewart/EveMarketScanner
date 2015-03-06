#Author: Jonathan Stewart
#Project: Eve Market Scanner

from SheetReader import *

#Book path
#***Prompt for sheet in future***
bookPath = 'invTypes.xls'
sheetNumber = 0

#Init utility classes
sheetReader = SheetReader()

#Init parameters
sheetReader.setBook(bookPath)
sheetReader.setSheet(sheetNumber)

#***TESTING***
print(sheetReader.hasMoreRows())
