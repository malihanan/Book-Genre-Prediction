import random

paragraph = """Thank you all so very much. Thank you to the Academy. Thank you to all of you in this room. I have to congratulate the other incredible nominees this year. The Revenant was the product of the tireless efforts of an unbelievable cast and crew. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your talent on screen can only be surpassed by your friendship off screen … thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency … my entire team. I have to thank everyone from the very onset of my career … To my parents; none of this would be possible without you. And to my friends, I love you dearly; you know who you are. And lastly, I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much."""
words = paragraph.split()

def create_ngram_letters(n):
	n_gram = {}
	for i in range(len(paragraph) - n):
	    if paragraph[i:i+n] not in n_gram.keys():
	        n_gram[paragraph[i:i+n]] = [paragraph[i+n]]
	    else:
	        n_gram[paragraph[i:i+n]].append(paragraph[i+n])
	return n_gram

def auto_complete_letters(n, n_gram, init = []):
	if len(init) < n:
		init = list(paragraph[:n])
	for i in range(n, len(paragraph)):
	    current_gram = ''.join(init[i-n:i])
	    if current_gram not in n_gram:
	        break
	    init.append(n_gram[current_gram][random.randrange(len(n_gram[current_gram]))])
	return(''.join(init))

def create_ngram_words(n):
	n_gram = {}
	for i in range(len(words) - n):
	    current_gram = ' '.join(words[i:i+n])
	    if current_gram not in n_gram.keys():
	        n_gram[current_gram] = [words[i+n]]
	    else:
	        n_gram[current_gram].append(words[i+n])
	return n_gram

def auto_complete_words(n, n_gram, init = []):
	if len(init) < n:
		init = [' '.join(words[:n])]
	for i in range(n, len(words)):
	    current_gram = ' '.join(words[i-n:i])
	    if current_gram not in n_gram:
	        break
	    init.append(n_gram[current_gram][random.randrange(len(n_gram[current_gram]))])
	return ' '.join(init)

if __name__ == '__main__':
	n = int(input("n: "))
	n_gram_letters = create_ngram_letters(n)
	print(auto_complete_letters(n, n_gram_letters))
	print()
	n_gram_words = create_ngram_words(n)
	print(auto_complete_words(n, n_gram_words))