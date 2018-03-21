import bot

def test_get():

    #Test 1:
    print (bot.get_access_token_secret())

    #Test 2:
    print (bot.get_access_token_key())

    #Test 3:
    print (bot.get_consumer_key())

    #Test 4: 
    print (bot.get_consumer_secret())


if __name__ == "__main__":
    test_get()
