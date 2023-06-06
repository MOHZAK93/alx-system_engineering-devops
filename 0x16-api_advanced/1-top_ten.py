#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of 10 hot posts
    listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """Prints the titles of 10 hot posts"""

    reddit_url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    header = {"User-Agent": "Chrome/81.0.404.129"}
    req = requests.get(reddit_url, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """Checks if response status is OK"""
        r_post = reddit.get("data").get("children")
        for post in r_post:
            print(post.get("data").get("title"))
    else:
        print("None")
