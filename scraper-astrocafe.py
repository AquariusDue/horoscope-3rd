import requests
import re
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url = "https://www.astrocafe.ro/horoscop/zilnic"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "lxml")

horoscopes_text = soup.select("#lvd-branding > article > p")

for index, horoscope in enumerate(horoscopes_text):
    horoscopes_text[index] = re.sub(r'<[^>]*>', '', str(horoscopes_text[index]))

horoscopes = {
        'berbec'    : horoscopes_text[0],
        'taur'      : horoscopes_text[1],
        'gemeni'    : horoscopes_text[2],
        'rac'       : horoscopes_text[3],
        'leu'       : horoscopes_text[4],
        'fecioara'  : horoscopes_text[5],
        'balanta'   : horoscopes_text[6],
        'scorpion'  : horoscopes_text[7],
        'sagetator' : horoscopes_text[8],
        'capricorn' : horoscopes_text[9],
        'varsator'  : horoscopes_text[10],
        'pesti'     : horoscopes_text[11]
    }

with open("horoscopes.json", "w") as outfile:
    json.dump(horoscopes, outfile)

print("Daily Horoscope succesfully updated")
