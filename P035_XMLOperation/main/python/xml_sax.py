'''
Created on Mar 9, 2024

@author: witek
'''
import xml.sax 

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "item":
            print("-----BOOK------")
            print("ISBN: {}".format(attrs['ISBN']))


    def characters(self, content):
        if self.current == "price":
            self.price = content
        elif self.current == "currency":
            self.currency = content

            
    def endElement(self, name):
        if self.current == "price":
            print("Price: {}".format(self.name))
        elif self.current == "currency":
            print("Currency: {}".format(self.name))
        self.current = ""
        
handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('sample.xml')