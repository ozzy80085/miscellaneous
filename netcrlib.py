import requests
from bs4 import BeautifulSoup
import re

def rating(site):
    page = requests.get(f"https://sitereport.netcraft.com/?url={site}")
    soup = BeautifulSoup(page.content, 'html.parser')
    filt = str(soup.find_all('span', class_='risk_label'))
    m = re.search('>(.+?)<', filt)
    rate = str(m.group(1))
    return rate