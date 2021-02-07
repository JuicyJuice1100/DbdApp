import requests
from bs4 import BeautifulSoup
import json
import os

IMAGETARGET = '../src/assets/images/'
BASEURL = 'https://deadbydaylight.fandom.com/wiki/'
SURVIVORSURL = BASEURL + 'Survivors'
KILLERSURL = BASEURL + 'Killers'
ITEMSURL = BASEURL + 'Items'
ITEMADDONSURL = BASEURL + 'Addons#Item_Add-ons' 
PERKSURL = BASEURL + 'Perks'

IMAGESPLIT = '/revision'

def getSoupPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def createJson(target, obj):
    with open(target, 'w') as outfile:
        outfile.write(obj)

def downloadImage(fileName, url):
    image = requests.get(url)

    target = IMAGETARGET + fileName

    with open(target, 'wb') as outfile:
        outfile.write(image.content)
