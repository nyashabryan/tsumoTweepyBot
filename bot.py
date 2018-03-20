# to a Twitter Account to post Tsumo every day. 

# Nyasha Katemauswa
# 19 March 2018


import tweepy


def main():
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
    except: 
        print('Error! Failed to get request token.')


    session.set('request_token', auth.request_token)

