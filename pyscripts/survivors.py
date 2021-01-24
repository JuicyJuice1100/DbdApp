import requests
from bs4 import BeautifulSoup
import json

def getSoupPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

BASEURL = 'https://deadbydaylight.fandom.com/wiki/'
survivorsURL = BASEURL + 'Survivors'
survivors = []
perks = []

survivorsPage = getSoupPage(survivorsURL)

survivorDiv = survivorsPage.find('span', id='List_of_Survivors').parent.find_next('div')

#go through each div and get survivor data
for div in survivorDiv:
    teachables = []


    name = div.find('a').text.replace(' ','_')
    image = div.find('img').get('src')

    survivorURL = BASEURL + name
    survivorPage = getSoupPage(survivorURL)

    #if description is long, get the first 500 chars and add link to survivor wiki
    description = survivorPage.find('span', id='Lore').parent.find_next('p').text
    if len(description) > 500:
        description = description[0:500] + '... ({})'.format(survivorURL)
    
    #get teachable names and levels, name will be used as ID
    ul = survivorPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('ul').find_all('li')

    for li in ul:
        perk = li.find('b').text
        level = [int(s) for s in li.text.split() if s.isdigit()][0]
        
        teachable = {'perk': perk, 'level': level}
        teachables.append(teachable)

    #get perk data
    table = survivorPage.find('span', id=lambda x: x and x.endswith('Perks')).parent.find_next('table').find_all('tr')

    for tr in table:
        data = tr.find_all('a')
        image = data[0].find('img').get('src')
        name = data[1].text

        descriptionArray = []

        for elm in tr.find('td').find_all('p'):
            descriptionArray.append(elm.text)

        description = ''.join([str(elem) for elem in descriptionArray])

        perk = {'name': name, 'image': image, 'description': description}
        perks.append(perk)

    survivor = {'name': name, 'image': image, 'description': description, 'teachables': teachables}
    survivors.append(survivor)

survivorsJson = json.dumps(survivors, indent = 4)
perksJson = json.dumps(perks, indent = 4)

with open('../src/assets/data/survivors.json', 'w') as outfile:
    outfile.write(survivorsJson)

with open('../src/assets/data/perks.json', 'w') as outfile:
    outfile.write(perksJson)

