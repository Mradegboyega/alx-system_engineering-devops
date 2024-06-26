#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent following redirects
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
