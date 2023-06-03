#!/usr/bin/python3
'''
Queries Reddit Api
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Queries Reddit Api for selected subreddit and returns no of subscribers
    Args:
        subreddit(str) - The name of the subreddit to check the no of subs
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers={'User-agent': 'Dragneel'})
    if data.status_code == 200:
        return data.json().get('data').get('subscribers')
    else:
        return 0
