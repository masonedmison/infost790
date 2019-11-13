"""get demographic data from American Fact Finder"""

import json
from lxml import html
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

ZIPS_= json.load(open('/home/medmison690/pyprojects/infost790/processing/mappings/zip_square_miles.json'))

BASE_URL = 'https://factfinder.census.gov//bkmk/table/1.0/en/DEC/10_DP/DPDP1/8600000US'
# https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=CF
def get_table_elems(html_):
    """get table elements within table using BeatifulSoup4)"""
    soup = BeautifulSoup(html_)
    print(soup)
    table_ = soup.find(id='data')
    for tr_ in table_:
        print(tr_)

# iter through zip in ZIPS_
print(ZIPS_)
for z in ZIPS_:
    full_z = BASE_URL + str(z.strip())
    print(full_z)
    resp = requests.get(full_z, headers=HEADERS)
    html_ = resp.text 
    print(html_)
    # get_table_elems(html_)
