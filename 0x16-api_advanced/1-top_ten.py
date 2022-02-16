#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the 1st 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 1st 10 hot posts of a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'user-agent': 'request'},
                            allow_redirects=False)
    if response.status_code != requests.codes.ok:
        print(None)
        return
    r = response.json()
    posts = r.get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
