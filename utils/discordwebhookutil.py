import requests
import time

webhook = ""


menu = """
[1] Send Message to Webhook
[2] Delete Webhook
"""

print(menu)
option = int(input("ur choice> "))

if option == 1:
	text = input("what message u wanna send> ")
	foo = requests.post(webhook, data={"Content-Type": "application/json", "content": text})
	if int(foo.status_code) == 204:
		print("Message Sent!")
		exit()

	if int(foo.status_code) == 429:
		print("ur being ratelimited!")
		exit()

	else:
		print(f"Unknown error! status code: {foo.status_code}")
		exit()

if option == 2:
	foo = requests.delete(webhook)
	if int(foo.status_code) == 204:
		print("Webhook Deleted!")
		exit()

	else:
		print(f"Unknown error! status code: {foo.status_code}")
                exit()
