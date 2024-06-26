#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent following redirects
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
