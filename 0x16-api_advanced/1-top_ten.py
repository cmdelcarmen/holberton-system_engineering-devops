#!/usr/bin/python3
'''
    Write a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''Prints the 1st 10 hot posts listed for a given subreddit'''
    URL = 'https://www.reddit.com/r/' + subreddit + '/top/.json?count=10'
    headers = 'Mozilla/5.0 (X11; Linux x86_64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/80.0.3987.87 Safari/537.36'
    response = requests.get(
            URL, allow_redirects=False, headers={'User-Agent': headers})
    try:
        count = 10
        response = response.json().get('data').get('children')
        for post in response:
            print(post.get('data').get('title'))
            count = count - 1
            if count == 0:
                break
    except:
        print(None)
