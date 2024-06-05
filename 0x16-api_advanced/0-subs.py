#!/usr/bin/python3
"""
Return the total number of subscribers on a given subreddit.
If an invalid subreddit is given, return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    If an invalid subreddit is given, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
