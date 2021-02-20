#!/usr/bin/env python
import requests
import re
import json
from bs4 import BeautifulSoup

urls = (
    ["berbec", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-berbec.php"],
    ["taur", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-taur.php"],
    ["gemeni", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-gemeni.php"],
    ["rac", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-rac.php"],
    ["leu", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-leu.php"],
    ["fecioara", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-fecioara.php"],
    ["balanta", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-balanta.php"],
    ["scorpion", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-scorpion.php"],
    ["sagetator", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-sagetator.php"],
    ["capricorn", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-capricorn.php"],
    ["varsator", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-varsator.php"],
    ["pesti", "https://www.eastrolog.ro/horoscop-zilnic/horoscop-pesti.php"],
)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

horoscopes = {}

# Request each link from urls
# Parse the html content and retrive the raw unedited daily horoscope text
# Edit the text with a regex to remove the <p> and <br> html tags
# Write the horoscope prediction along with the coresponding sign to the horoscopes dictionary
# Repeat for every astrological sign
for url in urls:
    page = requests.get(url[1], headers=headers)
    soup = BeautifulSoup(page.content, "lxml")
    horoscope_raw = soup.select(".contentLining > p")
    horoscope_pretty = re.sub(r'<[^>]*>', '', str(horoscope_raw[0]))
    horoscopes[url[0]] = horoscope_pretty

with open("horoscopes.json", "w") as outfile:
    json.dump(horoscopes, outfile)

print("Daily Horoscope succesfully updated")

# TODO: Add error catching and log file
