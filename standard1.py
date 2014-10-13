#!/usr/bin/python

from collections import defaultdict
import re
import sys

index = defaultdict(lambda: defaultdict(set))

for filename in sys.argv[1:]:
    lines = open(filename).read().splitlines()
    linenum = 0
    for line in lines:
        linenum += 1
        words = re.split('[^a-zA-Z0-9]+', line)
        for word in words:
            #or if linenum == last added linenum, also continue
            if word == '': continue
            index[word][filename].add(linenum)

for word in sorted(index):
    print word
    for filename in sorted(index[word]):
        print '\t', filename,
        for linenum in sorted(index[word][filename]):
            print linenum,
        print