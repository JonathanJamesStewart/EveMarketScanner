#Author: Jonathan Stewart
#Project: Eve Market Scanner

import xlrd
from Item import *

class SheetReader:

    #Init: initializes the reader.
    #Sets current row to 1
    def __init__(self):
        self.currentRow = 1
        self.items = []

    def __openSheet(self):
        book = xlrd.open_workbook(self.bookPath)
        sheet = book.sheet_by_index(self.sheetNumber)

        return sheet

    #Returns the next collection of items
    #***IMPLEMENT THIS METHOD***
    def getNextBatch(self, batchSize):
        #Reset items to be empty.
        self.items = []

        #Open the sheet
        sheet = self.__openSheet()

        #While the list is not full and there are more rows to read
        while (len(self.items) < batchSize) & (self.currentRow < sheet.nrows):

            #If the item is actually in the game add it to the list.
            if str(sheet.cell(self.currentRow, 4).value) != '':
                row = sheet.row(self.currentRow)
                item = Item(str(row[2].value), int(row[0].value))
                self.items.append(item)
            self.currentRow += 1

        return self.items
    
    #Sets the relative path of the book to read items from.
    def setBook(self, excelBookPath):
        self.bookPath = excelBookPath

    #Sets the sheet number
    def setSheet(self, sheetNumber):
        self.sheetNumber = sheetNumber

    #Determines if the sheet has more items that can be read.
    def hasMoreRows(self):
        sheet = self.__openSheet()
        
        if self.currentRow < sheet.nrows:
            return True
        return False
