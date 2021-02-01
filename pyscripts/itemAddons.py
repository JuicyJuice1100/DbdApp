import requests
from bs4 import BeautifulSoup
import json

def getSoupPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

BASEURL = 'https://deadbydaylight.fandom.com/wiki/'
itemAddonsUrl = BASEURL + 'Addons#Item_Add-ons' 

itemAddonsPage = getSoupPage(itemAddonsUrl)

itemIds = ['Flashlight', 'Key', 'Map', 'Med-Kit', 'Toolbox']
addons = []

for item in itemIds:
    trs = itemAddonsPage.find('span', id='Item_Add-ons').parent.find_next('span', id=item).parent.find_next('table').find_all('tr')

    for tr in trs[1:]:
        descriptionArray = []
        data = tr.find_all('a')

        image = data[0].find('img').get('src')
        addonName = data[1].text

        descriptionArray.append(tr.find('td').text)
        description = ''.join([elem for elem in descriptionArray])

        addon = {'item': item, 'image': image, 'addonName': addonName, 'description': description}
        addons.append(addon)

addonsJson = json.dumps(addons, indent = 4)

with open('../src/assets/data/itemAddons.json', 'w') as outfile:
    outfile.write(addonsJson)
    
