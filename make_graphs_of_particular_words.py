# -*- coding: utf-8 -*-
import csv
import copy
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open('p1.csv', 'rb') as f:
    reader = csv.reader(f)
    f1_0 = map(list, reader)
f1 = copy.deepcopy(f1_0)

with open('p2.csv', 'rb') as f:
    reader = csv.reader(f)
    f2_0 = map(list, reader)
f2 = copy.deepcopy(f2_0)

word_to_search = "yes"

x1 = []
y1 = []
total1 = 0
total_finds1 = 0

for word in f1:
	total1 += 1
	if word_to_search == word[1]:#[:len(word_to_search)]:
		total_finds1 += 1
		x1.append(datetime.strptime(word[0], "%Y-%m-%d %H:%M"))
		y_value = (float(total_finds1)/total1) * 1000
		y1.append(y_value)

x2 = []
y2 = []
total2 = 0
total_finds2 = 0

for word in f2:
	total2 += 1
	if word_to_search == word[1]:#[:len(word_to_search)]:
		total_finds2 += 1
		x2.append(datetime.strptime(word[0], "%Y-%m-%d %H:%M"))
		y_value = (float(total_finds2)/total2) * 1000
		y2.append(y_value)

plt.plot(x1, y1, 'r', x2 , y2, 'b')
red_patch = mpatches.Patch(color='red', label='Person 1')
blue_patch = mpatches.Patch(color='blue', label='Person 2')
plt.legend(handles=[red_patch,blue_patch])
#plt.axis([datetime.strptime(f1[0][0], "%Y-%m-%d %H:%M"), datetime.strptime(f1[len(f1)-1][0], "%Y-%m-%d %H:%M"), 0, 200])
plt.show()