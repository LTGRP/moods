import json
import sys
import os

data = []
with open(sys.argv[1]) as f:
    for line in f:
        data.append(json.loads(line))
    for item in data:
	print item['text']

