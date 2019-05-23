### GEO NEWS
import requests
from bs4 import BeautifulSoup

geopakistan = 'https://www.geo.tv/category/pakistan'
geosports = 'https://www.geo.tv/category/sports'
geoworld = 'https://www.geo.tv/category/world'
geosci = 'https://www.geo.tv/category/sci-tech'
geobus = 'https://www.geo.tv/category/business'

response = requests.get(geobus)
soup = BeautifulSoup(response.text, 'html.parser')

for featurenews in soup.select("#collapseOne1"):
    for sidenews in featurenews.select("li"):
        fnews = sidenews.h2.text


for topnews in soup.select("#collapseTwo1"):
    for sidenews in topnews.select("li"):
        fnews2 = sidenews.h2.text


######## Geo geopakistan
response = requests.get(geopakistan)
soup = BeautifulSoup(response.text, 'html.parser')
for mymainnews in soup.select(".singleBlock"):
    for mainpagenews in mymainnews.select(".entry-title"):
        mainnews = mainpagenews.h2.text
        print(mainnews)


######## Geo geoworld
response = requests.get(geoworld)
soup = BeautifulSoup(response.text, 'html.parser')
for mymainnews in soup.select(".singleBlock"):
    for mainpagenews in mymainnews.select(".entry-title"):
        mainnews = mainpagenews.h2.text
        print(mainnews)


######## Geo geosports
response = requests.get(geosports)
soup = BeautifulSoup(response.text, 'html.parser')
for mymainnews in soup.select(".singleBlock"):
    for mainpagenews in mymainnews.select(".entry-title"):
        mainnews = mainpagenews.h2.text
        print(mainnews)


######## Geo geosci
response = requests.get(geosci)
soup = BeautifulSoup(response.text, 'html.parser')
for mymainnews in soup.select(".singleBlock"):
    for mainpagenews in mymainnews.select(".entry-title"):
        mainnews = mainpagenews.h2.text
        print(mainnews)


######## Geo geobus
response = requests.get(geobus)
soup = BeautifulSoup(response.text, 'html.parser')
for mymainnews in soup.select(".singleBlock"):
    for mainpagenews in mymainnews.select(".entry-title"):
        mainnews = mainpagenews.h2.text
        print(mainnews)