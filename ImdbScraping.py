#### IMBD
import requests
from bs4 import BeautifulSoup

### Links
movie = 'https://www.imdb.com/news/movie'
tv = 'https://www.imdb.com/news/tv'
celebrity = 'https://www.imdb.com/news/celebrity'
intheaters = 'https://www.imdb.com/movies-in-theaters'
commingsoon = 'https://www.imdb.com/movies-coming-soon'
boxofficeweekend = 'https://www.imdb.com/chart/boxoffice'
besttvshow = 'https://www.imdb.com/chart/tvmeter'


response = requests.get(movie)
soup = BeautifulSoup(response.text, 'html.parser')
for moviehead in soup.select(".news-article__header"):
    movieheading = moviehead.h2.a.text
    print(movieheading)


response = requests.get(tv)
soup = BeautifulSoup(response.text, 'html.parser')
for tvhead in soup.select(".news-article__header"):
    tvheading = tvhead.h2.a.text
    print(tvheading)


response = requests.get(celebrity)
soup = BeautifulSoup(response.text, 'html.parser')
for celebhead in soup.select(".news-article__header"):
    celebheading = celebhead.h2.a.text
    print(celebheading)


response = requests.get(intheaters)
soup = BeautifulSoup(response.text, 'html.parser')
for intheatershead in soup.select(".overview-top"):
    intheatersheading = intheatershead.h4.a.text
    print(intheatersheading)


response = requests.get(commingsoon)
soup = BeautifulSoup(response.text, 'html.parser')
for commingsoonhead in soup.select(".overview-top"):
    commingsoonheading = commingsoonhead.h4.a.text
    print(commingsoonheading)


response = requests.get(boxofficeweekend)
soup = BeautifulSoup(response.text, 'html.parser')
for boxofficeweekendhead in soup.select(".titleColumn"):
    boxofficeweekendheading = boxofficeweekendhead.a.text
    print(boxofficeweekendheading)

for ratingboxofficehead in soup.select(".ratingColumn"):
    ratingboxofficeheading = ratingboxofficehead.text.strip()
    print(ratingboxofficeheading)


response = requests.get(besttvshow)
soup = BeautifulSoup(response.text, 'html.parser')
for besttvshowhead in soup.select(".titleColumn"):
    besttvshowheading = besttvshowhead.a.text
    print(besttvshowheading)

for besttvshowhead in soup.select(".ratingColumn"):
    for rating in besttvshowhead.find_all("strong"):
        ratingheading = rating.get_text()
        print(ratingheading)
