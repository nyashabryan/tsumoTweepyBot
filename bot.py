# to a Twitter Account to post Tsumo every day. 

# Nyasha Katemauswa
# 19 March 2018


import tweepy

keys_file = "keys"

def get_access_token_key():
    return get("access_token_key")

def get_access_token_secret():
    return get("access_token_secret")

def get_consumer_secret():
    return get("consumer_secret")

def get_consumer_key():
    return get("consumer_key")

def get(req):
    global keys_file
    with open(keys_file, "r:") as kfile:
	lines = kfile.readlines()
        for line in lines:
            if line.split(": ")[0] == req:
                return line.split(": ")[1][:-1]
    return "None"
	

def main():
    
    auth = tweepy.OAuthHandler(get_consumer_key(), get_consumer_secret())

    auth.set_access_token(get_access_token_key(), get_access_token_secret())
    
    api =  tweepy.API(auth)
    
    api.update_status("I am in this" )

if __name__ == "__main__":
    main()
