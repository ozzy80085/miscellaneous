import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--bytes", required=True, help="how many bytes")
parser.add_argument("-f", "--file", required=True, help="what file to save the bytes to")

args = parser.parse_args()

ransrc = f"https://www.random.org/cgi-bin/randbyte?nbytes={args.bytes}&format=h"

url = requests.get(ransrc)
data = (url.text)
print(f"{data}")

file = open(f"{args.file}", "w")
file.write(f"{data}")
file.close

print(f"Bytes saved to {args.file}")
