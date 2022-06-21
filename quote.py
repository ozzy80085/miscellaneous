import requests
from bs4 import BeautifulSoup

r = requests.get("http://quotes.toscrape.com/random", headers={"User-Agent": "https://github.com/ozzyisgreat/"})

soup = BeautifulSoup(r.text, "html.parser")

q = soup.find("div", {"class": "quote"})
quote = soup.find("span", {"class": "text"})
quote = "".join(quote.strings)

author = soup.find("small", {"class": "author"})
author = "".join(author.strings)

print(f"""
{quote}
        -{author}
""")
