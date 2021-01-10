from lib import *

soup = soup("https://www.wattpad.com/story/6141477-a-study-in-love-a-johnlock-fanfiction")
print(getPageUrl(soup))
print(len(getPageUrl(soup)))