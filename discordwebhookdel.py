import requests
import json

url = input("hello, please type the webhook url you wish to delete: ")

tok = requests.get(url)
if tok.status_code == 404:
	print("Sorry the webhook you specified does not exist")
	exit()

shit = json.loads(tok.text)

tokenraw = key, value = list(shit.items())[7]
tokenraw = str(tokenraw)

idraw = key, value = list(shit.items())[1]
idraw = str(idraw)

#remove all the extra token shit (im sure theres an easier way to do this but this method works so idc)
token = tokenraw.replace("token", "")
token = token.replace("\'", "")
token = token.replace(",", "")
token = token.replace("(", "")
token = token.replace(")", "")
token = token.replace(" ", "")

#do the same thing we did with the token but for the id
id = idraw.replace("id", "")
id = id.replace("\'", "")
id = id.replace(",", "")
id = id.replace("(", "")
id = id.replace(")", "")
id = id.replace(" ", "")


dele = requests.delete(f"https://discord.com/api/v9/webhooks/{id}/{token}")
if dele.status_code == 204:
	print("Webhook Deleted!")

if dele.status_code != 204:
	print(f"something's wrong, i can feel it (http status code: {dele.status_code}")
