import requests
from bs4 import BeautifulSoup

url1 = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/cena-do-650-eur-na-mesec/?s=16'
url2 = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/cena-do-650-eur-na-mesec/2/?s=16'
url3 = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/cena-do-650-eur-na-mesec/3/?s=16'
url4 = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/cena-do-650-eur-na-mesec/4/?s=16'
url5 = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/cena-do-650-eur-na-mesec/5/?s=16'

urls = [url1, url2, url3, url4, url5]

def check_new_ads(size_min, price_max):

    found_apartments = []

    responses = []
    for url in urls:
        try:
            r = requests.get(url)
            responses.append(r)
        except Exception as e:
            print('An error occurred in the request!', e)

    for response in responses:

        try:
            soup = BeautifulSoup(response.text, features="lxml")
            oglasi_tags = soup.find_all('div', itemtype="http://schema.org/Offer")

            for oglas_tag in oglasi_tags:
                cena = oglas_tag.find('span', class_='cena').text.split(' ')[0].replace(',','.')
                velikost = oglas_tag.find('span', class_='velikost').text.split(' ')[0].replace(',','.')
                lokacija = oglas_tag.find('span', class_='title').text
                link = oglas_tag.find('meta', itemprop='mainEntityOfPage')['content']

                if float(velikost)>=size_min and float(cena)<=price_max:
                    found_apartments.append((lokacija, velikost, cena, link))
                    # print('Stanovanje', lokacija, velikost, cena, link)
        except Exception as e:
            print('An error occurred in parsing the page', e)

    return found_apartments
