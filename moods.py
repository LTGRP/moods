import fileinput
import json
import sys
import os
from string import punctuation
from collections import Counter
import csv
import re 

line = []
pos=[]
neg=[]
exclude=[]
wordList=[]
posEmoList=[]
negEmoList=[]
neutralList=[]
hashtagList=[]
posTotalScore=0
negTotalScore=0

with open('preposition.dict') as f:
	exclude = [x.strip('\n') for x in f.readlines()]
	f.close()


with open('positive.dict') as f:
	pos = [x.strip('\n') for x in f.readlines()]
	f.close()


with open('negative.dict') as f:
 	neg = [x.strip('\n') for x in f.readlines()]
	f.close()

f = open(str(sys.argv[1]+'.csv'), 'wt')
writer = csv.writer(f)
writer.writerow(('Time', 'Followers', 'Emotion', 'Hashtags'))


smileys_positive = """:) :] :} :o) :D :o] :o} :-] :-) :-} =) =] =} =^] =^) =^} :B :-D :-B :^D :^B =B =^B =^D :')""".split()
                      
smileys_negative = """D: D= D-: D^: D^=""".split() 

pattern_pos = "|".join(map(re.escape, smileys_positive))
pattern_neg = "|".join(map(re.escape, smileys_negative))

inputfilename = sys.argv[1]
count=0
for line in fileinput.input([inputfilename]):
  try:	
	tweet = json.loads(line)
	count+=1
	flag=0
	posScore=0
	negScore=0
	emotion=0
	hashtags=[]
	try:
		hashtags=tweet['entities']['hashtags'][0]['text']
		hashtagList.append(hashtags)
	except Exception as e:
		pass
	tweettext=tweet['text'].lower()		
	for p in list(punctuation):
		tweettext=tweettext.replace(p,'')
	print "\nCount %d  "%count,
	print "Followers: %s " %tweet['user']['followers_count'],
	print " Time is %s " %tweet['created_at'],
	print " ", 	
	for word in tweettext.split():
	   if word not in exclude:	
		wordList.append(word)		
		if word in pos:
			print "pos: %s" %(word),
			posEmoList.append(word)
			flag=1
			posScore+=1
		elif word in neg:
			print "neg: %s" %(word),
			negEmoList.append(word)
			flag=1
			negScore+=1
	if((flag==0)or(negScore==posScore)):
		#emoticon quotient
		eq=len(re.findall(pattern_pos, tweettext))-len(re.findall(pattern_neg, tweettext))
		if(eq>0):
			posTotalScore+=1
			emotion=1
		elif(eq<0):
			negTotalScore+=1
			emotion=-1
		else:
			neutralList.append(tweet['text'])
	else:
		if(posScore>negScore):
			posTotalScore+=1
			emotion=1
		else:
			negTotalScore+=1
			emotion=-1
  	
	output=[tweet['created_at'],tweet['user']['followers_count'],emotion,hashtags]
	writer.writerow(output)
  except Exception as e:
	print('*** STOPPED %s' % str(e))
	pass


f.close()
print "\n\n\n"
print '*'*80
print '*'*80
c1 = Counter(wordList)
print "Most common words are"
print str(c1.most_common(10)).strip('[]')

print '*'*80
print '*'*80
c4 = Counter(hashtagList)
print "Most common hashtags are"
print str(c4.most_common(10)).strip('[]')

print '*'*80
print '*'*80
c2 = Counter(posEmoList)
print "Most common positive words are"
print str(c2.most_common(10)).strip('[]')
print "Tweets positive about it: %d" %posTotalScore

print '*'*80
print '*'*80
c3 = Counter(negEmoList)
print "Most common negative words are"
print str(c3.most_common(10)).strip('[]')
print "Tweets negative about it: %d" %negTotalScore

print '*'*80
print '*'*80

#Uncomment for debugging alogorithm
#for line in neutralList:
#	print line+"\n"

