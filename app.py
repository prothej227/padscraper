# Python PadScraper - Scrapes Wattpad Stories into PDF / ePUB
# Author: Journel Cabrillos
# Email: journelcabrillos@protonmail.com

from lib import getTitle, soup, getBody, getPageUrl, getChapTitle, getPageNum
import newGui

#story_url = input("Input url: ")

def storyMeta(url):

    ''' Crawls information about the story.\n 0 - Get Chapter urls, 1 - Get Story Title '''

    global story_url
    story_url = '%s' % url
    local_soup = soup(url)
    title = str(getTitle(local_soup))
    return [list(getPageUrl(local_soup)), title]

def scrapePage(pageNum, url):
    ''' Scrape pages per chapter '''
    txt = ""
    for z in range(pageNum):
        new_soup = soup(url + "/page/" + str(z))        
        newGui.updateLogs("Scraping contents from Page: " + str(z+1) + "\n")
        txt += str(getBody(new_soup))
    return txt

def initScrape(urlList):

    ''' Initialize Scrape Process '''

    txt = """
============================================
    Story/Book Title: {}
    Encoded: PadScraper v1
    Developer: Journel Cabrillos
============================================\n""".format(str(storyMeta(story_url)[1]))

    for i in range(len(urlList)):

        # Initialize new Soup
        url = "https://www.wattpad.com" + str(urlList[i])
        new_soup = soup(url)

        # Get Number of Chapters
        pageNum = getPageNum(url)

        # Update ProgressBar Status
        newGui.myLabel3.configure(text="Progress: [Scraping Chapter: " + str(i+1) + " of " + str(len(urlList)) + "]")
        newGui.myLabel3.update()

        # Update TextBox_Logs
        newGui.updateLogs(str("Scraping Chapter[{}]: {}".format((i+1), url)) + "\n")

        # Append Scraped text to string txt
        txt += """\n--------------------------------\n {} \n--------------------------------\n""".format(str(getChapTitle(new_soup)).rstrip())
        txt += scrapePage(pageNum, url)

        # Update ProgressBar value
        newGui.pbStep(len(urlList))

    return txt

def writeTxt(text):

    ''' Export Scraped Text to .txt File'''

    fname = '%s' % story_url
    fname = fname.replace("https://www.wattpad.com/story/", "").replace("/", "").replace('\'', "") + ".txt"
    f = open(fname, "a")
    f.write(text)
    f.close()
   

#writeTxt(initScrape(storyMeta(story_url)[0]))