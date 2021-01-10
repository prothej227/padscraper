# Python PadScraper - Scrapes Wattpad Stories into PDF / ePUB
# Author: Journel Cabrillos
# Email: journelcabrillos@protonmail.com

from lib import getTitle, soup, getBody, getPageUrl, getChapTitle, getPageNum

story_url = input("Input url: ")

def storyMeta(url):
    local_soup = soup(url)
    title = str(getTitle(local_soup))
    return [list(getPageUrl(local_soup)), title]

def scrapePage(pageNum, url):
    txt = ""
    for z in range(pageNum):
        new_soup = soup(url + "/page/" + str(z))        
        print("Scraping contents of Page: " + str(z+1))
        txt += str(getBody(new_soup))
    return txt

def initScrape(urlList):
    txt = """
============================================
    Story/Book Title: {}
    Encoded: PadScraper v1
    Developer: Journel Cabrillos
============================================\n""".format(str(storyMeta(story_url)[1]))

    for i in range(len(urlList)):
        url = "https://www.wattpad.com" + str(urlList[i])
        new_soup = soup(url)
        pageNum = getPageNum(url)
        print("Scraping Chapter[{}]: {}".format((i+1), url))
        txt += """\n--------------------------------\n {} \n--------------------------------\n""".format(str(getChapTitle(new_soup)).rstrip())
        txt += scrapePage(pageNum, url)

    return txt

def writeTxt(text):
    fname = '%s' % story_url
    fname = fname.replace("https://www.wattpad.com/story/", "").replace("/", "").replace('\'', "") + ".txt"
    f = open(fname, "a")
    f.write(text)
    f.close()

writeTxt(initScrape(storyMeta(story_url)[0]))