import json
import pythonHelper as pyHelper

#TODO clean up code

itemsPage = pyHelper.getSoupPage(pyHelper.ITEMSURL)

#{'category': [amount in category, letters to remove for category]}
itemIds = {'Firecrackers': [3, 1], 'Flashlights': [5,1], 'Keys': [3,1], 'Maps': [2, 1], 'Med-Kits': [6, 1], 'Toolboxes': [6,2]}
items = []

for k, v in itemIds.items():
    itemsTable = itemsPage.find('span', id=k).parent.parent.parent.find_next_siblings('tr', limit=v[0] + 1)
    for itemTable in itemsTable[1:]:
        descriptionArray = []

        data = itemTable.find_all('a')
        itemName = data[1].text

        fileName = itemName.replace(' ',  '_').replace('"','') + '.png'
        imageUrl = data[0].find('img').get('src')
        pyHelper.downloadImage(fileName, imageUrl)

        descriptionArray.append(itemTable.find('td').text)
        description = ''.join([elem for elem in descriptionArray])

        item = {'category': k[:-v[1]], 'image': fileName, 'itemName': itemName, 'description': description}

        items.append(item)

itemsJson = json.dumps(items, indent = 4)

pyHelper.createJson('../src/assets/data/items.json', itemsJson)