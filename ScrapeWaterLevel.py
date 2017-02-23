import unicodedata
from lxml import html
from lxml import etree
import requests
import pandas as pd
from xml.etree import ElementTree as ET


stanice={'bezdan':42010}
stanica='bezdan'
#number of days from today to be scraped
periodDays=7

page = requests.get('http://www.hidmet.gov.rs/latin/osmotreni/nrt_tabela_grafik.php?hm_id='+str(stanice[stanica])+'&period='+str(periodDays))
tree = html.fromstring(page.content)
vrednosti=[]
stanicaData= tree.xpath('//*[@id="sadrzaj"]/div/div[1]/table')

#t=etree.tostring(stanicaData[0],xml_declaration=False)
#print t
#parseStation(stanicaData)
rows = iter(stanicaData[0])
headers = [col.text for col in next(rows)]
print headers
for row in rows:
    for col in row:
        vrednosti.append(col.text)
print vrednosti
#unicodedata.normalize("NFKD",
#values = [col.text for col in row]

def parsestation(items):
    global lista
    for a in items:
        print etree.tostring(a)
        b = a.xpath('./div[@title="buyer-name"]')
        name = b[0].text
        b = a.xpath('./span[@class="item-price"]')
        price = b[0].text
        #add = etree.tostring(b[0], xml_declaration=False)
        lista.append([name,price])




print lista