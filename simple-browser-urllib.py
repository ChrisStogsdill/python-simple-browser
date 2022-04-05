import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

site = urllib.request.urlopen('https://en.wikipedia.org/wiki/Hygrocybe_miniata')
soup = BeautifulSoup(site, 'html.parser')
print(soup.prettify())
