# -*- coding: utf-8 -*-
import csv
import copy
import operator

with open('p1.csv', 'rb') as f:
    reader = csv.reader(f)
    f1_0 = map(list, reader)
f1 = copy.deepcopy(f1_0)

with open('p2.csv', 'rb') as f:
    reader = csv.reader(f)
    f2_0 = map(list, reader)
f2 = copy.deepcopy(f2_0)

p1 = []
p2 = []
p1p2 = []

for word in f1:
	if word[1] not in p1:
		p1.append(word[1])
	if word[1] not in p1p2:
		p1p2.append(word[1])

for word in f2:
	if word[1] not in p2:
		p2.append(word[1])
	if word[1] not in p1p2:
		p1p2.append(word[1])

print "Different words used by Person 1: " + str(len(p1))
print "Different words used by Person 2: " + str(len(p2))
print "Different words in the whole conversation: " + str(len(p1p2))