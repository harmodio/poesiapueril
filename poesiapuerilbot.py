import tweepy
from time import sleep

#Create variables for each key, secret, token
consumer_key = 'PzwW4qupC1qy3562g2wtCfMV1'
consumer_secret = 'wCivK4jYECDUbJCQBn9294EtGsYAgk2Z5V8wyLFM31tNjqNypW'
access_token = '869611298547421184-PfE7owxRC1RLC7bgzp14jdjvCcyjpyV'
access_token_secret = 'aU4r2FCuZtU5d6tR1LbfAbXb0r7MlcejbEso7OlSax7jI'
 
#Setup OAuth and integrate with API 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Write a tweet to push to our @poesiapueril account
#tweet = 'hola\nsoy\nun\nbot\nde\n#poesíapueril'
#api.update_status(status=tweet)

while True:
    for tweet in tweepy.Cursor(api.search, q='#poesíapueril').items():
        try:
            #Add \n escape character to print() to organize tweets
            print('\Tweet by @' + tweet.user.screen_name)

            #Retweets tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')

            sleep(1800)

        except tweepy.TweepError as e:
            print(e.reason)
            if e.message[0]['code']==185:
                print('Sleeping over a 185 error: User is over daily status limit')
                #Catching 'User is over daily status limit' error: we will wait
                sleep(1800)
     #end of the for: sleep 30min
    sleep(1800)
