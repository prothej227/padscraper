from lib import *

soup = soup("https://www.wattpad.com/707940886-and-the-music-played")
print(str(getChapTitle(soup)).rstrip())
print(len(getChapTitle(soup)))
print(getTitle(soup))