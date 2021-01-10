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
    try:
        return str(soup.find(class_="col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading").get_text()).replace("                          ", "")
    except Exception:
        pass
    return ""

# Get Page URLs
def getPageUrl(soup):
    tabOfContents = soup.find_all(class_="on-navigate-part")
    return [x.attrs['href'] for x in tabOfContents]

# Iterate through page numbers of each chapter
def getPageNum(url):
    n = 1
    while True:
        zsoup = soup(url + "/page/" + str(n))
        if  zsoup.find(attrs={"data-page-number": n}) != None:
            n = n + 1
        else:
            break
    return n-1