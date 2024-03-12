'''
Created on Mar 9, 2024

@author: witek
'''

import xml.etree.ElementTree as ET


if __name__ == "__main__":
    xml_doc = ET.Element('root')
    book = ET.SubElement(xml_doc, 'book')
    ET.SubElement(book, 'item', ISBN='9552251154444', price='99.99', currency='PLN').text = "Python"
    ET.SubElement(book, 'author', id='1').text='Jan Kowalski'
    
    tree = ET.ElementTree(xml_doc)
    tree.write('sample.xml')