import json
import pythonHelper as pyHelper

#TODO clean up code

survivors = []
perks = []

survivorsPage = pyHelper.getSoupPage(pyHelper.SURVIVORSURL)

survivorDiv = survivorsPage.find('span', id='List_of_Survivors').parent.find_next('div')

#go through each div and get survivor data
for div in survivorDiv:
    teachables = []

    survivorName = div.find('a').text
    
    fileName = survivorName.replace(' ',  '_').replace('"','') + '_portrait.png'
    imageUrl = div.find('img').get('src')
    pyHelper.downloadImage(fileName, imageUrl)

    survivorURL = pyHelper.BASEURL + survivorName.replace(' ','_')
    survivorPage = pyHelper.getSoupPage(survivorURL)

    #get overview
    overview = survivorPage.find('span', id='Overview').parent.find_next('p').text

    # #get lore
    # lore = survivorPage.find('span', id='Lore').parent.find_next('p').text
    
    #get teachable names and levels, name will be used as ID
    ul = survivorPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('ul').find_all('li')

    for li in ul:
        perk = li.find('b').text
        level = [int(s) for s in li.text.split() if s.isdigit()][0]
        
        teachable = {'perk': perk, 'level': level}
        teachables.append(teachable)

    # #get perk data
    # table = survivorPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('table').find_all('tr')

    # for tr in table:
    #     data = tr.find_all('a')

    #     perkImageUrl = data[0].find('img').get('src')
    #     perkImage = pyHelper.downloadImage(perkImageUrl)

    #     perkName = data[1].text

    #     descriptionArray = []

    #     for elm in tr.find('td').find_all('p'):
    #         descriptionArray.append(elm.text)

    #     description = ''.join([str(elem) for elem in descriptionArray])

    #     perk = {'perkName': perkName, 'image': perkImage, 'description': description}
    #     perks.append(perk)

    survivor = {'survivorName': survivorName, 'image': fileName, 'overview': overview, 'teachables': teachables}
    survivors.append(survivor)

survivorsJson = json.dumps(survivors, indent = 4)
perksJson = json.dumps(perks, indent = 4)

pyHelper.createJson('../src/assets/data/survivors.json', survivorsJson)
# pyHelper.createJson('../src/assets/data/survivorPerks.json', perksJson)