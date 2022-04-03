import praw
import time
import os
import sys

#https://www.reddit.com/prefs/apps to get key shit

reddit_read_only = praw.Reddit(client_id="", client_secret="", user_agent="")

subreddit = reddit_read_only.subreddit("teenagers")

print("Subreddit: ", subreddit.title, "\n")

try:
	while True:
		time.sleep(10)
		os.system("clear")
		for post in subreddit.new(limit=7):
			print("post title:", post.title)
			if post.selftext == "":
				post.selftext = "none"
			print("post text:", post.selftext)
			print("-" * 30)
except KeyboardInterrupt:
	print(" caught... exiting")
	sys.exit()
