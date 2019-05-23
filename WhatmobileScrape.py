#### Whatmobile
import requests
from bs4 import BeautifulSoup

### Links
samsung = 'https://www.whatmobile.com.pk/Samsung_Mobiles_Prices'
huawei = 'https://www.whatmobile.com.pk/Huawei_Mobiles_Prices'
oppo = 'https://www.whatmobile.com.pk/Oppo_Mobiles_Prices'
xiaomi = 'https://www.whatmobile.com.pk/Xiaomi_Mobiles_Prices'

response = requests.get(samsung)
soup = BeautifulSoup(response.text, 'html.parser')
for mobile in soup.select(".item"):
    mobileheading = mobile.a.find_next_sibling().text.strip()

for price in soup.select(".item"):
    allmobileprice = price.span.text
    mobileprice = allmobileprice.strip()

    mobileinfo = mobileheading + " " + mobileprice
    print(mobileinfo)