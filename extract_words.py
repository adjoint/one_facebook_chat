# -*- coding: utf-8 -*-
import csv
import re

chat = open("chat1.txt", "r")
lines = chat.readlines()

f1 = open("p1-1.csv", "w")
f2 = open("p2-1.csv", "w")
p1 = {}
p2 = {}

time = ""
i = 0
msg_count=0

while i < len(lines): 
	words = []
	if lines[i][:3] == "201":
		msg_count+=1			
		time = lines[i].strip("\n")
		#print time
		j = 0
		if "Person 1's name" in lines[i+1]:
			#print lines[i+1]
			j = i+2				
			while j < len(lines) and lines[j] != "\n":
				#print lines[j]
				words = lines[j].split(" ")
				new_words = []					
				for word in words:
					new_word = re.sub(r'\W+', '', word.lower().strip("\n"))
					try:
						f1.write(str(time) + "," + str(new_word) + "\n")
					except ValueError:
						print str(i) + " ERROR"
					new_words.append(new_word)
				if time not in p1:
					p1[time] = new_words
				else:
					p1[time].extend(new_words)
				j += 1
		elif "Person 2's name" in lines[i+1]:
			j = i+2
			while j < len(lines) and lines[j] != "\n":
				words = lines[j].split(" ")
				new_words = []
				for word in words:
					new_word = re.sub(r'\W+', '', word.lower().strip("\n"))
					try:
						f2.write(str(time) + "," + str(new_word) + "\n")
					except ValueError:
						print str(i) + " ERROR"
					new_words.append(new_word)
				if time not in p2:
					p2[time] = new_words
				else:
					p2[time].extend(new_words)
				j += 1
		if j!=0:
			i = j+1
		else:
			i = i+3
		print i
f1.close()
f2.close()
print msg_count


