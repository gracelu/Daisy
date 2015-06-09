#Grace Lu
#Homework 7: Arithmetic Compression
#program to compute left-to-right and right-to-left intervals of arithmetic encoding
 
# -*- coding: ascii -*-

import re 

phoneme_freq = {} #count up occurences of each phoneme
total_count = 0 #total number of phonemes
word_phonemes = {} #phonemes per word 

#read in dictionary file with phonemes
"""
with open("EnglishSmall.dx1") as infile:
	for line in infile:
		parts = line.split(' ') #find phonemes per each word

		pho_list = []

		#count phoneme occurences and add phonemes to word list
		for p in range(2, len(parts)):
			pho_list.append(parts[p].strip())
			total_count += 1
			try:
				phoneme_freq[parts[p].strip()] += 1
			except:
				phoneme_freq[parts[p].strip()] = 1

		word_phonemes[parts[0]] = pho_list
"""

with open('pire.txt') as infile:
	for line in infile:
		d = eval(line)
		#print d 
		#print d['keywords']
		for w in d['keywords']:
			pho_list = []
			#print w 
			#w = re.sub(r'[^a-zA-Z0-9]',' ', str(w))
			#print w 
			letters = re.sub(r'[^a-zA-Z0-9]',' ', w['value']).strip()
			print letters 
			for l in letters: #re.sub(r'[^a-zA-Z0-9]',' ', w['value']): #w['value'].strip():
				if l != ' ':
					pho_list.append(l.strip())
					total_count += 1
					try:
						phoneme_freq[l.strip()] += 1
					except:
						phoneme_freq[l.strip()] = 1

			#print pho_list
			#print phoneme_freq
			
			word_phonemes[letters] = pho_list

			#print word_phonemes

#compute intervals for each phoneme based on frequency
#spans a range of 0 to 1

starting_prange = {}
start = 0.0

for ph in sorted(phoneme_freq):
	end = start + float(phoneme_freq[ph])/float(total_count)
	starting_prange[ph] = (start, end)
	start = end

#keep track of start of left-to-right and right-to-left intervals for graph
x_coor = []
y_coor = []

for x in sorted(word_phonemes):

	factor = 1 #keep track of subsequent intervals
	begin = 0 #start of interval
	end = 0 #end of interval
	r = (0,1) #interval range

	#left to right computation
	for w in word_phonemes[x]:
		begin += factor * starting_prange[w][0]

		factor *= starting_prange[w][1] - starting_prange[w][0]
		
		end = begin + factor * starting_prange[w][1]

		r = (begin, end)

	factor = 1
	begin = 0
	end = 0
	r_rev = (0,1)

	#right to left computation
	for w in word_phonemes[x][::-1]:
		begin += factor * starting_prange[w][0]

		factor *= starting_prange[w][1] - starting_prange[w][0] 
		
		end = begin + factor * starting_prange[w][1]

		r_rev = (begin, end)

	#prints both intervals
	print x, r[0], r[1], r_rev[0], r_rev[1] 

	x_coor.append(r[0])
	y_coor.append(r_rev[0])

#plot graph of initial interval points
import matplotlib.pyplot as plt
pname = 'compression_graph.png'
plt.plot(x_coor, y_coor, 'ro')
plt.savefig(pname)
plt.clf()

"""
plt.plot(x_coor, y_coor, 'ro')
plt.show()
"""


