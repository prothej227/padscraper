# Python PadScraper - Scrapes Wattpad Stories into PDF / ePUB
# Author: Journel Cabrillos
# Email: journelcabrillos@protonmail.com

from lib import soup, getBody, getPageUrl, getChapTitle, getPageNum

def urlList(url):
    local_soup = soup(url)
    return getPageUrl(local_soup)

def scrapePage(pageNum, url):
    txt = ""
    for z in range(pageNum):
        new_soup = soup(url + "/page/" + str(z))        
        print("Scraping Page: " + str(z+1))
        txt += str(getBody(new_soup))
        return txt

def initScrape(urlList):
    txt = ""

    for i in range(len(urlList)):
        url = "https://www.wattpad.com" + urlList[i]
        new_soup = soup(url)
        pageNum = getPageNum(url)
        print("Scraping Chapter[{}]: {}".format((i+1), url))
        txt += scrapePage(pageNum, url)

    return txt

def writeTxt(text):
    f = open("padScrape.txt", "a")
    f.write(text)
    f.close()

writeTxt(initScrape(urlList("https://www.wattpad.com/story/6141477-a-study-in-love-a-johnlock-fanfiction")))