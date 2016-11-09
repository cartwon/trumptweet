#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
import string
import operator
from sets import Set

'''
states=['AK','Alaska','AL','Alabama','AZ','Arizona','AR','Arkansas','CA','California',\
    'CO','Colorado','CT','Connecticut','DE','Delaware','FL','Florida','GA','Georgia',\
    'HI','Hawaii','ID','Idaho','IL','Illinois','IN','Indiana', 'IA', 'Iowa',\
    'KS','Kansas','KY','Kentucky','LA', 'Louisiana','ME','Maine','MD', 'Maryland',\
    'MA','Massachusetts','MI', 'Michigan','MN', 'Minnesota', 'MS', 'Mississippi','MO', 'Missouri',\
    'MT','Montana','NE', 'Nebraska','NV','Nevada', 'NH', 'New Hampshire', 'NJ', 'New Jersey',\
    'NM','New Mexico','NY','New York','NC', 'North Carolina','ND', 'North Dakota','OH', 'Ohio',\
    'OK','Oklahoma','OR','Oregon','PA', 'Pennsylvania','RI', 'Rhode Island', 'SC', 'South Carolina',\
    'SD','South Dakota','TN', 'Tennessee','TX', 'Texas','UT', 'Utah','VT', 'Vermont',\
    'VA','Virginia','WA','Washington','DC','Washington DC','WV','West Virginia','WI','Wisconsin','WY','Wyoming']'''

def main():
    

    for line in sys.stdin:
        #generate features
        tweetLen=0           #1
        hashCount=0          #2
        puncCount=0          #3
        digitCount=0         #4
        stateDum=0           #5
        captCount=0          #6
        urlDum=0             #7
        exclamEndDum=0       #8
        wordCount=0          #9
        avgWordLen=0         #10
    
        line = line.strip()
        obs = line.split("\t") #a list of values
        label = obs[0]
        time = obs[1]
        tweet = obs[2] #a string
        words = tweet.split() #a list of words
            #for state in states:
            #if string.find(tweet,state)!=-1:
            #stateDum = 1
        
        if label=="Trump":
            label=+1
            tag="Trump"
        elif label=="Staff":
            label=-1
            tag="Staff"
        tweetLen = len(tweet)
        wordCount = len(words)
        avgWordLen = tweetLen / wordCount
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        puncCount = count(tweet, set(string.punctuation))
        captCount = count(tweet, set(string.ascii_uppercase))
        digitCount = count(tweet, set(string.digits))
        hashCount = count(tweet, set(['#']))
        
        if "https://" in tweet:
            urlDum = 1
        if tweet.endswith("!"):
            exclamEndDum=1
    
        features = "length:{0} punctuation:{1} capitals:{2} digits:{3} url:{4} exclamation:{5} wordcount:{6} avgchar:{7} hashtag:{8}".format\
(tweetLen,puncCount,captCount,digitCount,urlDum,exclamEndDum,wordCount,avgWordLen,hashCount)

        sep="| "
        out_string = str(label) + " " + tag + sep + features #
        print(out_string)

if __name__ == "__main__":
    main()

