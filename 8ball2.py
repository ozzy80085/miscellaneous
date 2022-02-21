#!/bin/python3
import random
import requests

ans = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As i see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

#make http request to random.org which returns 64 random bytes in hexadecimal
data = requests.get("https://www.random.org/cgi-bin/randbyte?nbytes=64&format=h")

#remove the spaces
data = data.text.replace(" ", "")

#remove the newline character at the end
data = data.strip()

#set the seed to data variable
random.seed(data)

#print the answer
print(random.choice(ans))
