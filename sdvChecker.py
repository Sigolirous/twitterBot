import tweepy as tweepy
import random as r
import time as t
data = open('data.txt', 'r')
keys = data.readlines
auth = tweepy.OAuthHandler(keys[1], keys[2])
auth.set_access_token(keys[4], keys[5])
api = tweepy.API(auth)
def checkSDV():
    followers = api.followers_ids('@Sigolirous')
    following = api.friends_ids('@Sigolirous')
    for follower in followers:
        euSigolo = follower in following
        if euSigolo == False :
            api.create_friendship(follower)
            print(f'Você vai seguir {follower}')
        else:
            print(f'Você já segue {follower}')            
while True:
    print('\n\n========================================================================\n\n')
    checkSDV()
    t.sleep(120)

