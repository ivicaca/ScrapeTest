from lxml import html
from lxml import etree
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
lista=[]

def parsePayer(items):
    global lista
    for a in items:
        print etree.tostring(a)
        b = a.xpath('./div[@title="buyer-name"]')
        name = b[0].text
        b = a.xpath('./span[@class="item-price"]')
        price = b[0].text
        #add = etree.tostring(b[0], xml_declaration=False)
        lista.append([name,price])


buyerInfo= tree.xpath('//div[@title="buyer-info"]')
parsePayer(buyerInfo)

print lista