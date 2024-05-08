#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    params = {'limit': 100}  # Maximum limit per request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)  # Prevent following redirects
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more pages (pagination) and recurse
        after = data['data'].get('after')
        if after:
            params['after'] = after
            recurse(subreddit, hot_list)

    elif response.status_code == 404:  # Subreddit not found
        return None

    return hot_list
