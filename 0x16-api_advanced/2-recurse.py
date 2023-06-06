"""Function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles"""
    reddit_url1 = "https://www.reddit.com/r/" + subreddit
    reddit_url2 = reddit_url1 + "/hot.json?limit=100&after=after"
    header = {"User-Agent": "Chrome/81.0.404.129"}
    req = requests.get(reddit_url2, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """Checks if the response status is OK"""
        hot_post = reddit.get("data").get("children")
        after = reddit.get("data").get("after")
        for posts in hot_post:
            hot_list.append(posts.get("data").get("title"))
        if after is None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
