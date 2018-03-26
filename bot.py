# to a Twitter Account to post Tsumo every day. 

# Nyasha Katemauswa
# 19 March 2018


import tweepy
import db

keys = db.get_keys()	

def main():
     
    auth = tweepy.OAuthHandler(keys[consumer_key], keys[consumer_secret])

    auth.set_access_token(keys[access_token_key], keys[access_token_secret])
    
    api =  tweepy.API(auth)
    
    api.update_status(db.get_tsumo())
    


if __name__ == "__main__":
    main()
