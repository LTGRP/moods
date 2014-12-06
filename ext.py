import fileinput
import json
import sys
import os
import nltk
from collections import Counter

line = []
pos=[]
neg=[]
wordList=[]
posEmoList=[]
negEmoList=[]


with open('positive.txt') as f:
	pos = [x.strip('\n') for x in f.readlines()]
	f.close()


with open('negative.txt') as f:
 	neg = [x.strip('\n') for x in f.readlines()]
	f.close()

inputfilename = sys.argv[1]

for line in fileinput.input([inputfilename]):
	tweet = json.loads(line)
	tweettext=tweet['text']
	for word in tweettext.lower().split():
		wordList.append(word)
		if word in pos:
			print "pos: %s" %word
			posEmoList.append(word)
		elif word in neg:
			print "neg: %s" %word
			negEmoList.append(word)


c1 = Counter(wordList)
print "Most common words are"
print c1.most_common(10)

c2 = Counter(posEmoList)
print "Most common positive words are"
print c2.most_common(10)
#print "Tweets positive about it: %d" %len(posEmoList)

c3 = Counter(negEmoList)
print "Most common negative words are"
print c3.most_common(10)
#print "Tweets positive about it: %d" %len(negEmoList)


