import json
import pprint
import sys
from TwitterAPI import TwitterAPI
from sys import argv
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib    
try:
    keyword=argv[1]
    api = TwitterAPI("JUTFW0LBNvkB645AoRJ8u8bN2", "X3TpSFPAlx0AWTe1LuNujBBriEOiXsDBARVUWlDkzE0fSEkiUV", "2851557234-dNayrWLxWS1LG8qfD42ygsUmSjTyunnvRwEl7sY", "uCBY0xb2aW8YXTWrLXV9dQTJoXKa0PLlKCquT9YOohqe8")
    tweets = []
    #print "Starting Twitter miner"
    r = api.request('statuses/filter', {'track':keyword})
    for item in r.get_iterator():
        try:
            print json.dumps(item, sort_keys=True)
        except:
            pass
except KeyboardInterrupt:
    #print('\nTerminated by user')
    for sample in tweets:
        try: 
            print sample['text'] +"end"
        except:
            pass
    #print "Exiting"
    

except Exception as e:
   print('*** STOPPED %s' % str(e))
   
   
#api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
#igraph
#networkx
#spyder
#pandas
#gephi
#plot.ly
#text2pdf -layout
