# Reddit API Tasks

This repository contains Python scripts that interact with the Reddit API to perform various tasks.

## Task 1: How many subs?

### Description
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.

### Requirements
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- Libraries: Use the Requests module for sending HTTP requests to the Reddit API.

## Task 2: Top Ten

### Description
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

### Requirements
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- Libraries: Use the Requests module for sending HTTP requests to the Reddit API.

## Task 3: Count it!

### Description
Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

### Requirements
- Prototype: `def count_words(subreddit, word_list)`
- If no posts match or the subreddit is invalid, print nothing.
- Libraries: Use the Requests module for sending HTTP requests to the Reddit API.
- The function should be recursive.
- The results should be printed in descending order of count, and alphabetically for words with the same count.

## Setup
- Ensure Python 3.4.3 or later is installed.
- Install the required libraries: `pip install requests`
- Clone this repository: `git clone https://github.com/example/reddit-api-tasks.git`
- Navigate to the project directory: `cd reddit-api-tasks`

## Usage
1. For Task 1:
   - Run the script `task1.py` and provide the subreddit name as an argument.

2. For Task 2:
   - Run the script `task2.py` and provide the subreddit name as an argument.

3. For Task 3:
   - Run the script `task3.py` and provide the subreddit name and a list of keywords as arguments.
