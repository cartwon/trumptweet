#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        obs = line.split("\t") #a list of values
        label = obs[0]
        time = obs[1]
        tweet = obs[2]
        words = tweet.split()
        
        #generate features
        wordCount=len(words) #1
        hashCount=0 #2
        puncaCount=0 #3
        numDum=0 #4
        stateDum=0 #5
        capCount=0 #6
        urlDum=0 #7
        
        if "state" in words:
            stateDum=1
        if "num" in words:
            numDum=1
        if "https" in words:
            urlDum=1
        

        
        
        
        if label=="Trump":
            label=1
            tag="Trump"
        elif:
            label=-1
            tag="Staff"
        
        sep="|"
        out_string = label + " " + tag + sep + features #
        print(out_string)
    
if __name__ == "__main__":
    main()
    
