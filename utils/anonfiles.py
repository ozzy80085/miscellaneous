import requests
import os

file = input("wut file u wanna upload: ")
files = { "file": (os.path.basename(file), open(file, "rb")), }
print("Uploading...")
foo = requests.post("https://api.anonfiles.com/upload", files=files)
if int(foo.status_code) != 200:
        print("Error\nStatus code: ", foo.status_code)
        exit()

data = foo.json()
url = data["data"]["file"]["url"]["short"]
rawsize = data["data"]["file"]["metadata"]["size"]["bytes"]
size = data["data"]["file"]["metadata"]["size"]["readable"]

print(f"""
{os.path.basename(file)} successfully uploaded
url: {url}
size: {size}({rawsize} bytes)
""")

