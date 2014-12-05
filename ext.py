import fileinput
import json
import sys
import os

line = []

inputfilename = sys.argv[1]

for line in fileinput.input([inputfilename]):
  tweettext = json.loads(line)
  print tweettext['text']
