from lxml import html
from lxml import etree
import requests

lista = []

brands = {'bmw':37, 'audi':38, 'opel':56, 'mercedes':175, 'peugeot':185}
brand='peugeot'

cc = 0

def process_list(items):
    global lista, cc
    for a in items:
        try:
            b = a.xpath('.//*[@class="itemtitle"]')
            naslov = b[0].getchildren()[0].text

            b = a.xpath('.//*[@class="title-km"]')
            km = b[0].text

            b = a.xpath('.//*[@class="title-year"]')
            year = b[0].text

            b = a.xpath('.//*[@class="title-price"]')
            price = b[0].text

            b = a.xpath('.//*[@class="ad-infobox"]')
            add = etree.tostring(b[0], xml_declaration=False)
            add = add.replace('\n', ' ').replace('\r', '').replace('\t', ' ')
            lista.append([str(cc), year, naslov, km, price, add[24:]])
        except Exception as ee:
            print ee
            pass
        cc += 1
        print cc


for i in range(120):
    page = requests.get('https://www.polovniautomobili.com/putnicka-vozila/pretraga?page='+str(i)+'&sort=renewDate_desc&brand='+str(brands[brand])+'&city_distance=0&without_price=1', verify=False)
    tree = html.fromstring(page.content)
    list_item = tree.xpath('//*[@class="item extend featured"]')
    process_list(list_item)
    list_item = tree.xpath('//*[@class="item extend "]')
    process_list(list_item)


with open("carsDb-"+brand+"_.csv", "a") as myfile:
    for it in lista:
        stri = ''
        for el in it:
            stri += str(el.encode('utf-8'))+'\t'
        myfile.write(stri+'\n')
