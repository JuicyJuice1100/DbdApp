import json
import pythonHelper as pyHelper

#TODO clean up code

survivorPerks = []
killerPerks = []

perksPage = pyHelper.getSoupPage(pyHelper.PERKSURL)

#Survivor Perks

survivorPerkTableData = perksPage.find('span', id=lambda x: x and x.startswith('Survivor_Perks')).parent.find_next('tbody').find_all('tr')

for row in survivorPerkTableData[1:]:
    imageElement = row.find_next('a')
    thElements = row.find_all('th')

    survivorPerkImageUrl = imageElement.find('img').get('src')
    survivorPerkName = thElements[1].text.replace(' ',  '_').replace('"','').replace('\n', '')
    survivorName = thElements[2].text.replace(' ',  '_').replace('"','').replace('\n', '')

    survivorPerkFileName = survivorPerkName.replace(' ',  '_').replace('"','').replace('\n', '') + '.png'
    pyHelper.downloadImage(survivorPerkFileName, survivorPerkImageUrl)
    
    descriptionArray = []

    for elm in row.find('td').find_all('p'):
        descriptionArray.append(elm.text)

    survivorPerkDescription = ''.join([str(elem) for elem in descriptionArray])

    survivorPerk = {'survivorTeachable': survivorName, 'perkName': survivorPerkName, 'image': survivorPerkFileName, 'description': survivorPerkDescription}
    survivorPerks.append(survivorPerk)

survivorPerksJson = json.dumps(survivorPerks, indent = 4)

pyHelper.createJson('../src/assets/data/survivorPerks.json', survivorPerksJson)

#Killer Perks

killerPerkTableData = perksPage.find('span', id=lambda x: x and x.startswith('Killer_Perks')).parent.find_next('tbody').find_all('tr')

for row in killerPerkTableData[1:]:
    imageElement = row.find_next('a')
    thElements = row.find_all('th')

    killerPerkImageUrl = imageElement.find('img').get('src')
    killerPerkName = thElements[1].text.replace(' ',  '_').replace('"','').replace('\n', '')
    killerName = thElements[2].text.replace(' ',  '_').replace('"','').replace('\n', '')

    killerPerkFileName = killerPerkName.replace(' ',  '_').replace('"','').replace('\n', '') + '.png'
    pyHelper.downloadImage(killerPerkFileName, killerPerkImageUrl)
    
    descriptionArray = []

    for elm in row.find('td').find_all('p'):
        descriptionArray.append(elm.text)

    killerPerkDescription = ''.join([str(elem) for elem in descriptionArray])

    killerPerk = {'killerTeachable': killerName, 'perkName': killerPerkName, 'image': killerPerkFileName, 'description': killerPerkDescription}
    killerPerks.append(killerPerk)

killerPerksJson = json.dumps(killerPerks, indent = 4)

pyHelper.createJson('../src/assets/data/killerPerks.json', killerPerksJson)