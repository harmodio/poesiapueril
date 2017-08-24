#/usr/bin/env python3
# -*- coding: utf8 -*-
##
## Copyright (c) 2017 Jorge Harmodio

##     poesiapuerilbot is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.

##     poesiapuerilbot is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.

##     You should have received a copy of the GNU General Public License
##     along with Unoporuno.  If not, see <http://www.gnu.org/licenses/>.


import tweepy
import time
#from time import sleep

import logging
#Create variables for each key, secret, token
consumer_key = 'PzwW4qupC1qy3562g2wtCfMV1'
consumer_secret = 'wCivK4jYECDUbJCQBn9294EtGsYAgk2Z5V8wyLFM31tNjqNypW'
access_token = '869611298547421184-PfE7owxRC1RLC7bgzp14jdjvCcyjpyV'
access_token_secret = 'aU4r2FCuZtU5d6tR1LbfAbXb0r7MlcejbEso7OlSax7jI'
 

#Write a tweet to push to our @poesiapueril account
#tweet = 'hola\nsoy\nun\nbot\nde\n#poesíapueril'
#api.update_status(status=tweet)
logging.basicConfig(level=logging.INFO)
logging.info("Starting execution of poesiapuerilbot on " + time.asctime())
       


while True:
    #Setup OAuth and integrate with API 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:

        for tweet in tweepy.Cursor(api.search, q='#poesíapueril').items():
            try:
                #Add \n escape character to print() to organize tweets
                logging.info('\Tweet by @' + tweet.user.screen_name)

                #Retweets tweets as they are found
                tweet.retweet()
                logging.info('Retweeted the tweet:ready to sleep')

                time.sleep(1800)

            except tweepy.TweepError as e:
                logging.error(str(e.reason))
                if e.args[0][0]['code']==185:
                    logging.info('Sleeping over a 185 error: User is over daily status limit')
                    #Catching 'User is over daily status limit' error: we will wait
                    time.sleep(1800)
                elif e.args[0][0]['code']==327:
                    logging.error('Repeated tweet')

         #end of the for: sleep 30min
        time.sleep(1800)
    except IOError as ex:
        logging.error(str(ex))
