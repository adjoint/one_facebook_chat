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

p1 = {}
p2 = {}

total1 = 0
total2 = 0

for word in f1:
	total1 += 1
	if word[1]!="":
		if word[1] not in p1:
			p1[word[1]] = 1
		else:
			p1[word[1]] += 1

for word in f2:
	total2 += 1
	if word[1]!="":
		if word[1] not in p2:
			p2[word[1]] = 1
		else:
			p2[word[1]] += 1

sorted_p1 = sorted(p1.items(), key=operator.itemgetter(1), reverse=True)
sorted_p2 = sorted(p2.items(), key=operator.itemgetter(1), reverse=True)

print "Total words by Person 1:" + str(total1)
print "Total words by Person 2:" + str(total2)
print "20 most common words by Person 1:"
print sorted_p1[:20]
print "20 most common words by Person 2:"
print sorted_p2[:20]