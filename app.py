from lib import soup, getBody, getPageUrl, getChapTitle

url = "https://www.wattpad.com/477671236-sherlock-holmes-a-study-in-scarlet-by-sir-arthur"

def initScrape(url):
    txt = ""
    new_soup = soup(url)
    urlList = getPageUrl(new_soup)
    txt += str(getBody(new_soup))

    for i in range(1, len(urlList)):
        nextPageUrl = str("https://www.wattpad.com" + urlList[i])
        print("Scraping Chapter[{}]: {}".format(i+1, nextPageUrl))
        lsoup = soup(nextPageUrl)
        txt +=  str(getBody(lsoup))

    return txt

def writeTxt(text):
    f = open("padScrape.txt", "a")
    f.write(text)
    f.close()

writeTxt(initScrape(url))