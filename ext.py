import fileinput
import json
import sys
import os
from collections import Counter

line = []
pos=[]
neg=[]
wordList=[]
posEmoList=[]
negEmoList=[]
neutralList=[]


with open('positive.txt') as f:
	pos = [x.strip('\n') for x in f.readlines()]
	f.close()


with open('negative.txt') as f:
 	neg = [x.strip('\n') for x in f.readlines()]
	f.close()

inputfilename = sys.argv[1]
count=0
for line in fileinput.input([inputfilename]):
	tweet = json.loads(line)
	count+=1
	flag=0
	tweettext=tweet['text'].lower().replace('!','').replace('#','')
	for word in tweettext.split():
		wordList.append(word)
		if word in pos:
			print "%d pos: %s" %(count,word)
			posEmoList.append(word)
			flag=1
		elif word in neg:
			print "%d neg: %s" %(count,word)
			negEmoList.append(word)
			flag=1
	if(flag==0):
		neutralList.append(tweet['text'])

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

for line in neutralList:
	print line+"\n"

