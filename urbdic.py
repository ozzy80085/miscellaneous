import requests
import feedparser

feed = feedparser.parse("http://feeds.urbandictionary.com/UrbanWordOfTheDay")

def entry(num):
        word = feed.entries[num].title
        define = feed.entries[num].description
        for i in "[]":
                define = define.replace(i, "")
        return f"\nWord: {word}\nDefinition: {define}\n"
 

print(entry(0))
      
#for i in range(3):
#        print(entry(i))

