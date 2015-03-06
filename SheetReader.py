#Author: Jonathan Stewart
#Project: Eve Market Scanner

import xlrd

class SheetReader:

    #Init: initializes the reader.
    #Sets current row to 1
    def __init__(self):
        self.currentRow = 1
        self.items = []

    #Returns the next collection of items
    #***IMPLEMENT ITEM CLASS***
    #***IMPLEMENT THIS METHOD***
    def getNextBatch(batchSize):
        return 0
    
    #Sets the relative path of the book to read items from.
    def setBook(self, excelBookPath):
        self.bookPath = excelBookPath

    #Sets the sheet number
    def setSheet(self, sheetNumber):
        self.sheetNumber = sheetNumber

    #Determines if the sheet has more items that can be read.
    def hasMoreRows(self):
        book = xlrd.open_workbook(self.bookPath)
        sheet = book.sheet_by_index(self.sheetNumber)
        
        if self.currentRow < sheet.nrows:
            return True
        return False
