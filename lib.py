# Python PadScraper - Scrapes Wattpad Stories into PDF / ePUB
# Author: Journel Cabrillos
# Email: journelcabrillos@protonmail.com

# Libraries
from bs4 import BeautifulSoup
import requests

# Init Soup
def soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Get Story Title
def getTitle(soup):
    mainTitle = soup.find(class_="title_h5")
    return mainTitle

# Get Chapter Title
def getChapTitle(soup):
    return soup.find(class_="h2").get_text()
    
# Returns a clean text containing the story paragraphs    
def getBody(soup):
    return str(soup.find(class_="col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading").get_text()).replace("                          ", "")

# Get Page URLs
def getPageUrl(soup):
    tabOfContents = soup.find_all(class_="on-navigate")
    return [x.attrs['href'] for x in tabOfContents if tabOfContents.index(x) in range(31, len(tabOfContents)- 26)]

# 
def getPageNum(soup):
    return None
