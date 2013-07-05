from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
	mymap={}
	
	for i,j in enumerate(strlist):
		for word in j.split():
			
			if word  in mymap:
				mymap[word].add(i)
			else:
				mymap[word]=set({i})
		
	return mymap

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    return  set.union(*[inverseIndex[i] for i in query])
    #pass

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    return  set.intersection(*[inverseIndex[i] for i in query])
