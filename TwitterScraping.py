#### Twitter Account
import requests
from bs4 import BeautifulSoup

### Links
twiteraccount = 'https://twitter.com/JohnCena'

response = requests.get(twiteraccount)
soup = BeautifulSoup(response.text, 'html.parser')
for account in soup.find_all(class_="js-stream-item stream-item stream-item"):
    for accountin in account.select(".tweet-text"):
        anyaccount = accountin.text
        print(anyaccount)
