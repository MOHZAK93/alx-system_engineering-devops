#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers"""

    reddit_url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "Chrome/81.0.404.129"}
    req = requests.get(reddit_url, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """Checks if response status is ok"""
        subs = reddit.get("data").get("subscribers")
        return (subs)
    else:
        return 0
