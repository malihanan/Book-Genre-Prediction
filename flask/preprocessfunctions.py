import nltk
try:
    from nltk.corpus import stopwords
except:
    nltk.download('stopwords')
    from nltk.corpus import stopwords
try:
    from nltk.tokenize import punkt
except:
    nltk.download('punkt')
    from nltk.tokenize import punkt
    
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from num2words import num2words
import numpy as np
import re as re
stop_words = set(stopwords.words('english'))

def remove_stopwords(data):
    global stop_words

    word_tokens = word_tokenize(str(data))

    filtered_data = ""

    for w in word_tokens:
        if w not in stop_words and len(w) > 1:
            filtered_data = filtered_data + " " + w
    return filtered_data


def remove_punctuation(data):
    marks = "~!@#$%^&*()_+=-`[]\;'./{}|:<>?""'\n"

    for i in marks:
        data = np.char.replace(data, i, ' ')
        data = np.char.replace(data, "  ", " ")

    data = np.char.replace(data, ",", '')
    return data


def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


def stemming(data):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))

    new_text = ""

    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)

    return new_text


def lemmatize(data):
    wnl = WordNetLemmatizer()
    tokens = word_tokenize(str(data))

    new_text = ""

    for w in tokens:
        new_text = new_text + " " + wnl.lemmatize(w)

    return new_text


def convert_numbers(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:

        try:
            w = num2words(int(w))
        except:
            pass
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text


def preprocess(data):
    data = np.char.lower(data)

    data = remove_punctuation(data)  # remove comma seperately

    data = remove_apostrophe(data)

    data = remove_stopwords(data)

    data = convert_numbers(data)

    data = stemming(data)

    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data)  # needed again as we need to stem the words
    data = remove_punctuation(data)  # needed again as num2word is giving few hypens and commas fourty-one
    data = remove_stopwords(data)  # needed again as num2word is giving stop words 101 - one hundred and one
    return data


def preprocesswithoutstem(data):
    data = np.char.lower(data)

    data = remove_punctuation(data)  # remove comma seperately

    data = remove_apostrophe(data)

    data = remove_stopwords(data)

    data = convert_numbers(data)

    #     data = stemming(data)

    data = remove_punctuation(data)
    #     data = stemming(data) #needed again as we need to stem the words
    #     data = remove_punctuation(data)
    data = convert_numbers(data)
    data = remove_stopwords(data)  # needed again as num2word is giving stop words 101 - one hundred and one
    return data


def clean_text(text):
    text = re.sub("\'", "", text)
    text = re.sub("[^a-zA-Z]"," ",text)
    text = ' '.join(text.split())
    text = text.lower()
    return text


def remove_stopwords1(text):
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)

