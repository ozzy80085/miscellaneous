import requests
import bs4

r = requests.get("https://www.coindesk.com/price/bitcoin/")

soup = bs4.BeautifulSoup(r.text, features="lxml")

price = soup.find("span", {"class": "typography__StyledTypography-owin6q-0 ktzuAh"})
price = "".join(price.strings)

hr = soup.find("h6", {"class": "typography__StyledTypography-owin6q-0 bclXpS"})
hr = "".join(hr.strings)

print(f"""Current BTC Price: {price}
The price has changed {hr} in the last 24 hours
""")

