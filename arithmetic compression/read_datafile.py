import re

phoneme_freq = {} #count up occurences of each phoneme
total_count = 0 #total number of phonemes
word_phonemes = {} #phonemes per word

with open('data_sample.txt') as infile:
	for line in infile:
		d = eval(line)
		#print d 
		#print d['keywords']
		for w in d['keywords']:
			pho_list = []
			#print w 
			#w = re.sub(r'[^a-zA-Z0-9]',' ', str(w))
			#print w 
			letters = re.sub(r'[^a-zA-Z0-9]',' ', w['value'])
			print letters 
			for l in letters: #re.sub(r'[^a-zA-Z0-9]',' ', w['value']): #w['value'].strip():
				if l != ' ':
					pho_list.append(l.strip())
					total_count += 1
					try:
						phoneme_freq[l.strip()] += 1
					except:
						phoneme_freq[l.strip()] = 1

			print pho_list
			print phoneme_freq

					
			word_phonemes[w['value']] = pho_list

			#print word_phonemes
