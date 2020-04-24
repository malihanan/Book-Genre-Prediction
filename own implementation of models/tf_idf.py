import nltk
import re
import heapq
import math
import numpy as np
from nltk.corpus import stopwords
'''
def generate_words(dataset):
	words = []
	for data in dataset:
		for word in nltk.word_tokenize(data):
			words.append(word)
	return words
'''
def clean_data(dataset):
	for i in range(len(dataset)):
	    dataset[i] = dataset[i].lower()
	    dataset[i] = re.sub(r'\W', ' ', dataset[i])
	    dataset[i] = re.sub(r'\s+', ' ', dataset[i])
	    dataset[i] = re.sub('^\s+', '', dataset[i])
	    dataset[i] = re.sub(r'\s$', '', dataset[i])
	return dataset


def create_word_count(words):
	word_count = {}
	for word in words:
		if word in word_count.keys():
			word_count[word] += 1
		else:
			word_count[word] = 1
	return word_count

def create_idf(dataset, words):
	idf = {}
	for word in words:
	    t = 0
	    for data in dataset:
	        if word in data:
	            t+=1;
	    idf[word] = np.log((len(dataset)+1)/(t+1))
	return idf

def create_tf(dataset, words):
	'''
	tf = []
	for i in range(len(dataset)):
	    vector = []
	    w = nltk.word_tokenize(dataset[i])
	    for j in range(len(most_freq_words)):
	        vector.append(w.count(most_freq_words[j]) / len(w))
	    tf.append(vector)
	tf = np.asarray(tf)
	return tf
	'''
	tf = {}
	for word in words:
		doc_tf = []
		for data in dataset:
			freq = 0
			for w in nltk.word_tokenize(data):
				if w == word:
					freq += 1
			doc_tf.append(freq/len(nltk.word_tokenize(data)))
		tf[word] = doc_tf
	return tf

def create_tfidf(dataset, most_freq_words):
	tf = create_tf(dataset, most_freq_words)
	idf = create_idf(dataset, most_freq_words)
	tfidf = []
	for word in tf.keys():
	    t = []
	    for value in tf[word]:
	        t.append(idf[word]*value)
	    tfidf.append(t)
	tfidf = np.asarray(tfidf)
	tfidf = np.transpose(tfidf)
	return tfidf

def get_sorted_words(tfidf, words):
	s = {}
	for i in range(tfidf.shape[0]):
	    for j in range(tfidf.shape[1]):
	        if(tfidf[i][j] != 0):
	            if words[i] in s.keys():
	                s[words[i]] += tfidf[i][j]
	            else:
	                s[words[i]] = tfidf[i][j]
	return sorted(s.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

def create_feautures(s):
	i=0
	features=[]
	for key, value in s:
	    features.append(key)
	    i+=1
	    if i == 10:
	        break
	return features

def generate_features(paragraph):
	#generate NNPs
	dataset = nltk.sent_tokenize(paragraph)
	words = [word for data in dataset for word in nltk.word_tokenize(data)]
	nnp_words = [item[0].lower() for item in nltk.pos_tag(words) if item[1] == 'NNP']

	dataset = clean_data(dataset)
	words = [word for data in dataset for word in nltk.word_tokenize(data)]

	#remove stop words and NNPs
	stop_words = stopwords.words('english')
	words = [word for word in words if word not in stop_words and word not in nnp_words]

	word_count = create_word_count(words)
	most_freq_words = heapq.nlargest(math.ceil(len(word_count.keys())*0.5), word_count)
	
	tfidf = create_tfidf(dataset, most_freq_words)
	s = get_sorted_words(tfidf, most_freq_words)
	features = s[:10]
	return [item[0] for item in features]

if __name__ == '__main__':
	paragraph = input("Paragraph: ")
	features = generate_features(paragraph)
	print(features)