# to a Twitter Account to post Tsumo every day. 

# Nyasha Katemauswa
# 19 March 2018


import tweepy
import db
import random
import sys

keys = db.get_keys()	

def post_tsumo():
    
    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])

    auth.set_access_token(keys["access_token"], keys["access_token_secret"])
    
    api =  tweepy.API(auth)
    
    x =  random.randint(1, db.get_tsumo_count())
    api.update_status(db.get_tsumo(x))

    print ("Tsumo number ", x, " has been posted successfully")

if __name__ == "__main__":
    args = (sys.argv)
    
    if args[1] == "post":
        post_tsumo()

