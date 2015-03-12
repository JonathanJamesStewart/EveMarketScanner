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

    #Build the URL
    def __buildURL(self, items):
        #Create a temporary address so we don't override the master
        self.tempAddress1 = self.address1
        self.tempAddress2 = self.address2

        #Add all item ids
        for item in items:
            self.tempAddress1 = self.tempAddress1 + self.typeID + str(item.itemID) + '&'
            self.tempAddress2 = self.tempAddress2 + str(item.itemID) + ','

        #Remove the last comma
        self.tempAddress2 = self.tempAddress2[:len(self.tempAddress2) - 1]
        
        #Add last parts to the address
        self.tempAddress1 += self.sys + str(self.systemID)

        self.tempAddress2 += self.char_name + self.charName
        self.tempAddress2 += self.regionIDs + str(self.regionID)
        self.tempAddress2 += self.days + str(self.numDays)

    #Extract the information received from query 1
    def __extractFromAddress1(self, XMLResult, items):
        maxBuy = 0
        minSell = 0

        #Convert the XML to a tree.
        tree = ET.fromstring(XMLResult)

        #Drill down the tree until we find the information we want.
        #Mainly maxBuy and minSell.
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
                #Find the item in the list and update the values.
                for item in items:
                    if str(item.itemID) == str(node.attrib['id']):
                        item.maxBuy = maxBuy
                        item.minSell = minSell

    #Extract the information received from query 2
    def __extractFromAddress2(self, XMLResult, items):
        tree = ET.fromstring(XMLResult)

        #Drill down the tree until we find the information we want.
        #Mainly volume.
        for node in tree.getiterator():
            if node.tag == 'row':
                #Find the item in the list and update the values.
                for item in items:
                    if str(item.itemID) == str(node.attrib['typeID']):
                        item.volume += int(node.attrib['volume'])
                        item.volumeCount += 1

    #Build the URL and query the site.
    def querySite(self, items):
        self.__buildURL(items)

        #Query1
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

        #Query 2
        while True:
            try:
                f2 = urllib.request.urlopen(self.tempAddress2)
                break
            except:
                print(self.tempAddress2)
                sys.exit(self.tempAddress2)
                pass
        volumeFromXML = f2.read()

        self.__extractFromAddress2(volumeFromXML, items)

    #Setters for properties. Probably not needed but the code works without
    #and I don't want to change it since it doesn't sacrifice much performance
    #or functionality.
    def setSystemID(self, systemID):
        self.systemID = systemID

    def setRegionID(self, regionID):
        self.regionID = regionID

    def setCharName(self, charName):
        self.charName = charName

    def setNumDays(self, numDays):
        self.numDays = numDays
        
