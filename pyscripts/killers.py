import requests
from bs4 import BeautifulSoup
import json

def getSoupPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

BASEURL = 'https://deadbydaylight.fandom.com/wiki/'
killersURL = BASEURL + 'Killers'
killers = []
perks = []

killersPage = getSoupPage(killersURL)

killerDiv = killersPage.find('span', id='List_of_Killers').parent.find_next('div')

#go through each div and get killer data
for div in killerDiv:
    teachables = []


    characterName = div.find('a').text.replace(' ','_')
    killerName = div.find('img').parent.get('title')
    image = div.find('img').get('src')

    killerURL = BASEURL + characterName.replace(' ','_')
    killerPage = getSoupPage(killerURL)

    #if overview is long, get the first 500 chars and add link to killer wiki
    overview = killerPage.find('span', id='Overview').parent.find_next('p').text
    if len(overview) > 500:
        overview = overview[0:500] + '... ({})'.format(killerURL)

    #if lore is long, get the first 500 chars and add link to killer wiki
    lore = killerPage.find('span', id='Overview').parent.find_next('p').text
    if len(lore) > 500:
        lore = lore[0:500] + '... ({})'.format(killerURL)
    
    #get teachable names and levels, name will be used as ID
    ul = killerPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('ul').find_all('li')

    for li in ul:
        perk = li.find('b').text
        level = [int(s) for s in li.text.split() if s.isdigit()][0]
        
        teachable = {'perk': perk, 'level': level}
        teachables.append(teachable)

    #get perk data
    table = killerPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('table').find_all('tr')

    for tr in table:
        data = tr.find_all('a')
        image = data[0].find('img').get('src')
        perkName = data[1].text

        descriptionArray = []

        for elm in tr.find('td').find_all('p'):
            descriptionArray.append(elm.text)

        description = ''.join([str(elem) for elem in descriptionArray])

        perk = {'name': perkName, 'image': image, 'description': description}
        perks.append(perk)

    killer = {'killerName': killerName, 'characterName': characterName, 'image': image, 'overview': overview, 'lore': lore,'teachables': teachables}
    killers.append(killer)

killersJson = json.dumps(killers, indent = 4)
perksJson = json.dumps(perks, indent = 4)

with open('../src/assets/data/killers.json', 'w') as outfile:
    outfile.write(killersJson)

with open('../src/assets/data/killerPerks.json', 'w') as outfile:
    outfile.write(perksJson)