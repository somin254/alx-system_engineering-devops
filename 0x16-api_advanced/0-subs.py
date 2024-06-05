#!/usr/bin/python3
"""
Return the total number of subscribers on a given subreddit.
If an invalid subreddit is given, return 0.
"""

import json
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    If an invalid subreddit is given, return 0.
    """
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException:
        return 0
