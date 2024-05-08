#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    params = {'limit': 100}  # Maximum limit per request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)  # Prevent following redirects

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()  # Convert title to lowercase for case-insensitive comparison
            for word in word_list:
                if word.lower() in title:
                    count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

        # Check if there are more pages (pagination) and recurse
        after = data['data'].get('after')
        if after:
            params['after'] = after
            count_words(subreddit, word_list, count_dict)

    elif response.status_code == 404:  # Subreddit not found
        return

    if not count_dict:  # No matches found
        return

    # Print results in descending order of count, and alphabetically for words with the same count
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
