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

x1 = []
y1 = []
total1 = 0

for word in f1:
	total1 += 1
	x1.append(datetime.strptime(word[0], "%Y-%m-%d %H:%M"))
	y1.append(total1)

x2 = []
y2 = []
total2 = 0

for word in f2:
	total2 += 1
	x2.append(datetime.strptime(word[0], "%Y-%m-%d %H:%M"))
	y2.append(total2)

plt.plot(x1, y1, 'r', x2 , y2, 'b')
red_patch = mpatches.Patch(color='red', label='Person 1')
blue_patch = mpatches.Patch(color='blue', label='Person 2')
plt.legend(handles=[red_patch,blue_patch])
plt.show()
