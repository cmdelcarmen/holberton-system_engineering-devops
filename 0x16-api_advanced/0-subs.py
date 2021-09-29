#!/usr/bin/python3
'''
    Write a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
'''

import requests


def number_of_subscribers(subreddit):
    '''Method gets the number of subs for a subreddit'''
    URL = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = 'Mozilla/5.0 (X11; Linux x86_64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/80.0.3987.87 Safari/537.36'
    response = requests.get(
            URL, allow_redirects=False, headers={'User-Agent': headers})

    try:
        return response.json().get('data').get('subscribers')
    except:
        return 0
