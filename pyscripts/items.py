import requests
from bs4 import BeautifulSoup
import json

def getSoupPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

BASEURL = 'https://deadbydaylight.fandom.com/wiki/'
itemsUrl = BASEURL + 'Items'

itemsPage = getSoupPage(itemsUrl)

#{'category': [amount in category, letters to remove for category]}
itemIds = {'Firecrackers': [3, 1], 'Flashlights': [5,1], 'Keys': [3,1], 'Maps': [2, 1], 'Med-Kits': [6, 1], 'Toolboxes': [6,2]}
items = []

for k, v in itemIds.items():
    itemsTable = itemsPage.find('span', id=k).parent.parent.parent.find_next_siblings('tr', limit=v[0] + 1)
    for itemTable in itemsTable[1:]:
        descriptionArray = []

        data = itemTable.find_all('a')

        image = data[0].find('img').get('src')
        itemName = data[1].text

        descriptionArray.append(itemTable.find('td').text)
        description = ''.join([elem for elem in descriptionArray])

        item = {'category': k[:-v[1]], 'image': image, 'itemName': itemName, 'description': description}

        items.append(item)

itemsJson = json.dumps(items, indent = 4)

with open('../src/assets/data/items.json', 'w') as outfile:
    outfile.write(itemsJson)