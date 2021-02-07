import json
import pythonHelper as pyHelper

#TODO clean up code

itemAddonsPage = pyHelper.getSoupPage(pyHelper.ITEMADDONSURL)

itemIds = ['Flashlight', 'Key', 'Map', 'Med-Kit', 'Toolbox']
addons = []

for item in itemIds:
    trs = itemAddonsPage.find('span', id='Item_Add-ons').parent.find_next('span', id=item).parent.find_next('table').find_all('tr')

    for tr in trs[1:]:
        descriptionArray = []
        data = tr.find_all('a')

        addonName = data[1].text

        fileName = addonName.replace(' ',  '_').replace('"','') + '.png'
        imageUrl = data[0].find('img').get('src')
        pyHelper.downloadImage(fileName, imageUrl)


        descriptionArray.append(tr.find('td').text)
        description = ''.join([elem for elem in descriptionArray])

        addon = {'item': item, 'image': fileName, 'addonName': addonName, 'description': description}
        addons.append(addon)

addonsJson = json.dumps(addons, indent = 4)

pyHelper.createJson('../src/assets/data/itemAddons.json', addonsJson)
    
