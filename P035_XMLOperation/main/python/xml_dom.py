'''
Created on Mar 9, 2024

@author: witek
'''
import xml.dom.minidom

domtree = xml.dom.minidom.parse('sample.xml')
group = domtree.documentElement

books = group.getElementsByTagName('book')

for book in books:
    print('-----BOOK-----')
    if book.hasAttribute('id'):
        print("ID: {}".format(book.getAttribute('id')))

    print("Title:  {}".format(book.getElementsByTagName('item')[0].childNodes[0].data))
    print("Author: {}".format(book.getElementsByTagName('author')[0].childNodes[0].data))
    
books[2].getElementsByTagName('item')[0].childNodes[0].nodeValue = "New title"
books[0].setAttribute('id','1000')

#domtree.writexml(open('example.xml'))

newbook = domtree.createElement('book')
newbook.setAttribute('id','6')

item = domtree.createElement('item')
item.appendChild(domtree.createTextNode("Ansible"))

author = domtree.createElement('author')
author.appendChild(domtree.createTextNode("Stanisław Kowalski"))

newbook.appendChild(item)
newbook.appendChild(author)

group.appendChild(newbook)

domtree.writexml(open('sample.xml', 'w'))