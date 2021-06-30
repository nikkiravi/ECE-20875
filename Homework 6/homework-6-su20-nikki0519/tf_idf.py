
from helper import remove_punc
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk.tokenize as tk
import numpy as np
from itertools import chain
import math


#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    file = open(doc, 'r')
    info = file.read()

    #2. Tokenize string using nltk.tokenize.word_tokenize
    nltk.download('punkt')
    tokens_step2 = tk.word_tokenize(info)

    #3. Filter out punctuation from list of words (use remove_punc)
    tokens_step3 = remove_punc(tokens_step2)

    #4. Make the words lower case 
    lower_case = [i.lower() for i in tokens_step3]

    #5. Filter out stopwords
    nltk.download('stopwords')
    stop_word = stopwords.words('english')
    clean_tokens = [words for words in lower_case if words not in stop_word]

    #6. Stem words
    nltk.download('wordnet')

    stemmer = PorterStemmer()
    stemm_clean_tokens = [stemmer.stem(words) for words in clean_tokens]

    return stemm_clean_tokens
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordlist = [readAndCleanDoc(i) for i in doclist]

    unique_list = []

    for word in wordlist:
        for w in word:
            unique_list.append(w)

    unique_words = set(unique_list)

    sorted_word_list = sorted(list(unique_words))

    #2. Use these word lists to build the doc word matrix
    docword = np.zeros((len(doclist), len(sorted_word_list)))

    for index, word in enumerate(wordlist):
        for w in word:
            docword[index, sorted_word_list.index(w)] += 1
    
    wordlist = sorted_word_list

    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    tf = np.asarray([[num / sum(row) for num in row] for row in docword])

    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in

    idf = np.log10(docword.shape[0] / np.sum(docword > 0, axis = 0).reshape(1, -1))

    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in

    tfidf = buildTFMatrix(docword) * buildIDFMatrix(docword)


    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html

    tfidf = buildTFIDFMatrix(docword)

    for i in range(len(doclist)):
        l = list(tfidf[i, :])

        idx1 = int(l.index(max(l)))
        l[idx1] = -1

        idx2 = int(l.index(max(l)))
        l[idx2] = -1

        idx3 = int(l.index(max(l)))
        l[idx3] = -1


        distinctiveWords[doclist[i]] = [wordlist[idx1], wordlist[idx2], wordlist[idx3]]

    return distinctiveWords

if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    
    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***") 
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
    
