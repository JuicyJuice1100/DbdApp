import json
import pythonHelper as pyHelper

#TODO clean up code

killers = []
perks = []

killersPage = pyHelper.getSoupPage(pyHelper.KILLERSURL)

killerDiv = killersPage.find('span', id='List_of_Killers').parent.find_next('div')

#go through each div and get killer data
for div in killerDiv:
    teachables = []
    power = []
    addons = []

    characterName = div.find('a').text.replace(' ','_')
    killerName = div.find('img').parent.get('title')

    portraitFileName = killerName.replace(' ',  '_').replace('"','') + '_portrait.png'
    imageUrl = div.find('img').get('src')
    pyHelper.downloadImage(portraitFileName, imageUrl)

    killerURL = pyHelper.BASEURL + characterName.replace(' ','_')
    killerPage = pyHelper.getSoupPage(killerURL)

    #if overview is long, get the first 500 chars and add link to killer wiki
    overview = killerPage.find('span', id='Overview').parent.find_next('p').text
    # if len(overview) > 500:
    #     overview = overview[0:500] + '... ({})'.format(killerURL)

    # #if lore is long, get the first 500 chars and add link to killer wiki
    # lore = killerPage.find('span', id='Lore').parent.find_next('p').text
    # # if len(lore) > 500:
    # #     lore = lore[0:500] + '... ({})'.format(killerURL)
    
    #get teachable names and levels, name will be used as ID
    ul = killerPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('ul').find_all('li')

    for li in ul:
        perk = li.find('b').text
        level = [int(s) for s in li.text.split() if s.isdigit()][0]
        
        teachable = {'perk': perk, 'level': level}
        teachables.append(teachable)

    # #get perk data
    # teachableTable = killerPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('table').find_all('tr')

    # for tr in teachableTable:
    #     data = tr.find_all('a')
    #     perkImage = data[0].find('img').get('src')
    #     perkName = data[1].text

    #     descriptionArray = []

    #     for elm in tr.find('td').find_all('p'):
    #         descriptionArray.append(elm.text)

    #     description = ''.join([str(elem) for elem in descriptionArray])

    #     perk = {'perkName': perkName, 'image': perkImage, 'description': description}
    #     perks.append(perk)

    #get power data
    powerName = killerPage.find('span', id=lambda x: x and x.startswith('Power')).text.replace('Power: ', '')
    powerDescriptionElements = killerPage.find('span', id=lambda x: x and x.startswith('Power')).parent.find_next_siblings('p')

    powerDescription = ''.join([elem.text for elem in powerDescriptionElements])
    
    power = {'powerName': powerName, 'powerDescription': powerDescription }

    #get add-ons
    addonTable = killerPage.find('span', id=lambda x: x and x.startswith('Add-ons')).parent.find_next('table').find_all('tr')

    for tr in addonTable[1:]:
        descriptionArray = []

        data = tr.find_all('a')
        addonName = data[1].text

        addonFileName = addonName.replace(' ',  '_').replace('"','') + '.png'
        addonImageUrl = data[0].find('img').get('src')
        pyHelper.downloadImage(addonFileName, addonImageUrl) 

        descriptionArray.append(tr.find('td').text)

        description = ''.join([elem for elem in descriptionArray])

        addon = {'addonName': addonName, 'image': addonFileName, 'description': description}
        addons.append(addon)

    killer = {'killerName': killerName, 'characterName': characterName, 'image': portraitFileName, 'overview': overview, 'power': power, 'teachables': teachables, 'addons': addons}
    killers.append(killer)

killersJson = json.dumps(killers, indent = 4)
# perksJson = json.dumps(perks, indent = 4)

pyHelper.createJson('../src/assets/data/killers.json', killersJson)
# pyHelper.createJson('../src/assets/data/killerPerks.json', perksJson)