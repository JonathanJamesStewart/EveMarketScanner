#Author: Jonathan Stewart
#Project: Eve Market Scanner

import urllib.request
import xml.etree.ElementTree as ET
import sys

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
        for item in items:
            self.address1 = self.address1 + self.typeID + str(item.itemID) + '&'
            self.address2 = self.address2 + str(item.itemID) + ','
        self.address2 = self.address2[:len(self.address2) - 1]

        self.address1 += self.sys + str(self.systemID)

        self.address2 += self.char_name + self.charName
        self.address2 += self.regionIDs + str(self.regionID)
        self.address2 += self.days + str(self.numDays)

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
                f1 = urllib.request.urlopen(self.address1)
                break
            except:
                print(self.address1)
                sys.exit(self.address1)
                pass
        itemsFromXML = f1.read()
        while True:
            try:
                f2 = urllib.request.urlopen(self.address2)
                break
            except:
                print(self.address2)
                sys.exit(self.address2)
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
        
