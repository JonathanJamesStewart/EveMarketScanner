#Author: Jonathan Stewart
#Project: Eve Market Scanner

import urllib.request
import xml.etree.ElementTree as ET
import sys
from decimal import Decimal

class Query:

    def __init__(self):
        self.address1 = 'http://api.eve-central.com/api/marketstat?'
        self.address2 = 'http://api.eve-marketdata.com/api/item_history2.xml?type_ids='
        self.typeID = 'typeid='
        self.sys = 'usesystem='
        self.char_name = '&char_name='
        self.regionIDs = '&region_ids='
        self.days = '&days='

        self.systemID = 0
        self.regionID = 0
        self.charName = ''
        self.numDays = 0

    def __buildURL(self, items):
        self.tempAddress1 = self.address1
        self.tempAddress2 = self.address2
        
        for item in items:
            self.tempAddress1 = self.tempAddress1 + self.typeID + str(item.itemID) + '&'
            self.tempAddress2 = self.tempAddress2 + str(item.itemID) + ','
        self.tempAddress2 = self.tempAddress2[:len(self.address2) - 1]

        self.tempAddress1 += self.sys + str(self.systemID)

        self.tempAddress2 += self.char_name + self.charName
        self.tempAddress2 += self.regionIDs + str(self.regionID)
        self.tempAddress2 += self.days + str(self.numDays)

    def __extractFromAddress1(self, XMLResult, items):
        maxBuy = 0
        minSell = 0
        
        tree = ET.fromstring(XMLResult)

        for node in tree.getiterator():
            if node.tag == 'type':
                for child in node:
                    if child.tag == 'buy':
                        for base in child:
                            if base.tag == 'max':
                                maxBuy = Decimal(base.text)
                    if child.tag == 'sell':
                        for base in child:
                            if base.tag == 'min':
                                minSell = Decimal(base.text)
                for item in items:
                    if str(item.itemID) == str(node.attrib['id']):
                        item.maxBuy = maxBuy
                        item.minSell = minSell

    def __extractFromAddress2(self, XMLResult, items):
        tree = ET.fromstring(XMLResult)

        if node.tag == 'row':
            for item in items:
                if str(item.itemID) == str(node.attrib['typeID']):
                    item.volume += int(node.attrib['volume'])
                    item.volumeCount += 1

    def querySite(self, items):
        self.__buildURL(items)

        while True:
            try:
                f1 = urllib.request.urlopen(self.tempAddress1)
                break
            except:
                print(self.tempAddress1)
                sys.exit(self.tempAddress1)
                pass
        itemsFromXML = f1.read()
        
        self.__extractFromAddress1(itemsFromXML, items)
        while True:
            try:
                f2 = urllib.request.urlopen(self.tempAddress2)
                break
            except:
                print(self.tempAddress2)
                sys.exit(self.tempAddress2)
                pass
        volumeFromXML = f2.read()

    def setSystemID(self, systemID):
        self.systemID = systemID

    def setRegionID(self, regionID):
        self.regionID = regionID

    def setCharName(self, charName):
        self.charName = charName

    def setNumDays(self, numDays):
        self.numDays = numDays
        
