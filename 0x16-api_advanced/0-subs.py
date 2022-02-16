#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'user-agent': 'request'},
                            allow_redirects=False)
    if response.status_code != requests.codes.ok:
        return 0
    r = response.json()
    subs = r.get('data').get('subscribers')
    return subs
