## Sets and functions - Chapter0 ##

# No. of minutes in a week
7*24*60*60


# To find the remainder
2304811%47


# Use of Boolean operaters
(673+909)%3 == 0


# Use of conditional expressions
x = -9
y = 1/2

2**(y+1/2) if x+10<0 else 2**(y-1/2)


''' Sets '''
{1+2,3,'a'}
{2,1,3}
 

# Cardinality of a set
len({'a','b','c','a','a'})


#Summing of elements
sum({1,2,3})
sum({1,2,3},10)


#testing the membership of an element
1 in {1,2,3}
1 not in {1,2,3}


# Union and intersection of sets
{1,2,3,4} | {3,4,5,6}
{1,2,3,4} & {3,4,5,6}


# Mutating a set
S = {1,2,3}
S.add(4)
S.remove(2)
S.update({4,5,6})
S.intersection_update({4,5,6})

# to copy a data structure
T = S.copy()

# Set Comprehensions
{2*x for x in {1,2,3} }
{x**2 for x in {1,2,3,4,5} }
{2**x for x in {0,1,2,3,4} }

# Set comprehension with union and intersection
{x*x for x in S | {5,7}}

{x*x for x in S | {5,7} if x > 2}

# Double Comprehension
{x*y for x in {1,2,3} for y in {4,5,6}}

#Double Comprehension with a filter
{x*y for x in {1,2,3} for y in {2,3,4} if x!=y}

S = {1,2,3,4}
T = {3,4,5,6}
{x for x in S for y in T if x==y}

################### Lists #######################

# lists allow duplicate items
[1,1+1,2,3,2]

# a list contain a set, another list
[[1,1+1,3],{2*2,3,5},"yo"]

len([[1,1+1,3],{2*2,3,5},"yo","yo"])

# Sum of a list
sum([1,1,0,1,0,1])

# list concatenation
[1,2,3] + ["my","word"]

# using Sum function for concatenation of lists
sum([[1,2,3]  ["my","word"]],[])

# List Comprehensions
[2*x for x in {2,1,3,4}]

[2*x for x in [2,1,3,4]]

# Double Comprehension in lists
[x*y for x in [1,2,3] for y in [10,20,30]]

[[x,y] for x in ['A','B','C'] for y in [1,2,3]]

# Caluculating sum of all elemnts in a list
LofL = [[.25,.75,.1],[-1,0],[4,4,4,4]]
sum([sum(LofL[0]),sum(LofL[1]),sum(LofL[2])])

# Indexing of List
L = [0,10,20,30,40,50,60,70,80,90]
L[:5]
L[5:]

# Slice the cth element
L[::2] # Index with even numbers
L[1::2] # Index with odd numbers

# assingning a list of variables
[x,y,z] = [4*1, 4*2, 4*3]

############## Tuples ##################
(1,1+1,3)

# Tuples(immutable) can be a part of the set
{0,(1,2)} | {(3,4,5)}

# A set can be a element of Tuples
(1,{"A","B"},3.14)[2]

# Unpacking with tuples
(a,b) = (1,3)

# a list of tuples sum of each tuples is 0
[(x,y,z) for x in S for y in S for z in S if x+y+z == 0]
[(x,y,z) for x in S for y in S for z in S if x+y+z == 0 and (x,y,z) != (0,0,0)]
[(x,y,z) for x in S for y in S for z in S if (x,y,z) == (0,0,0)]

# Obtaining a list or set from other collection
set([0,1,2,3,4,4])
set((0,1,2,3,4,4))

list({0,1,2,3,4,4})
list((0,1,2,3,4,4))

tuple([0,1,2,3,4,4])
tuple({0,1,2,3,4,4})

# We can not iterate over tuples
(x for x in (1,2,3)) # this won't work as it is a generator

# ranges are arthematic progressions
{x*x for x in range(10)}
# a range is not a list
list(range(10))

range(10,20) # a sequence between 10 to 20
range(10,20,2) # a sequence between 10 to 20 with a jump of 2

# Zip is constructed from other collection of same length
zip([1,2,3],[3,4,5])

characters = ['Neo','Morepheus','Trinity']
actors = ['keanu','Launrence','Carrie-Anne']
set(zip(characters,actors))

[characters+' is played by '+actors for (characters,actors) in zip(characters,actors)]

######
L = ['A','B','C','D','E']
list(zip(range(5),L))

[x+y for (x,y) in zip([10,25,40],[1,15,20])]

# reversers changes the order of the list
[x for x in  reversed([1,2,3])]


################ Dictionaries ########################
# key:value
{2:'two',3:'three',5:'five'}
{2:'two',3:'three',5:'five'}.keys()
{2:'two',3:'three',5:'five'}.values()

# indexing into dictionary
{2:'two',3:'three',5:'five'}[2]
mydict = {'Neo': 'keanu','Morepheus':'Laurence','Trninity':'Carrie-Anne'}
mydict['Neo']

# testing the membership 
'Neo' in mydict

# tasks in dictionaries
dlist = [{'James':'Sean','director':'Terence'},{'James':'Roger','director':'Lewis'},{'James':'Pierce','director':'Roger'}]
[x['James'] for x in dlist]
################################

dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
[x['Bilbo'] if 'Bilbo' in x else 'NotPresent' for x in dlist]
[x['Frodo'] if 'Frodo' in x else 'NotPresent' for x in dlist]

### Mutating a dictionary 
mydict = {'Neo': 'keanu','Morepheus':'Laurence','Trninity':'Carrie-Anne'}
mydict['Agent Smith'] = 'Hugo'

###### Dictionary Comprehension #######
{k:v for (k,v) in [(3,2),(4,0),(100,1)]}

#### tasks in dictionaries ############
{x:x**2 for x in range(100)}

D = {'red','white','blue'}
{x:x for x in D}

########################################
base = 10
digits = set(range(base))
{x:[a,b,c] for x in range(10) for a in digits for b in digits for c in digits if (base**2)*a+(base**1)*b+(base**0)*c == x}

a.keys()|b.keys()
a.keys()&b.keys()

# changing the dictionary in a tuple
mydict.items()

id2salary = {0:1000.0, 3:900,1:1200.50}
names = ['Larry','Curly','Moe']

{k:v for (k,v) in set(zip(names, [x for (y,x) in list(id2salary.items())]))}
{names[x]:id2salary[x] for x in id2salary.keys()} # mapping the names to the salary

################ One - line Procedures #####################
def twice(z) : return 2*z

def nextInts(L) : return [x+1 for x in L]

def cubes(L) : return [z**3 for z in L]

def dict2list(dct,keylist) : return [dct[x] for x in keylist]

def list2dict(L, keylist) : return {keylist[x]:L[x] for x in range(len(keylist))}

def all_3_digits_number(base,digits): return [x for x in range(100) for a in digits for b in digits for c in digits if (base**2)*a+(base**1)*b+(base**0)*c == x]

############## Inbuilt module ################
import math
from random import randint

randint(1,5)

review = ['See it!','A gem!','Ideological claptrap']

def movie_review(name) : return(review[randint(0,len(review))])

movie_review('Ground Hog Day')

import dictutil

from imp import reload

# split strings in python
mystr = 'Ask not what you can do for your country'
mystr.split()

# enumerate
list(enumerate(['A','B','C']))

import os
os.chdir("C:\\Users\\Ankit\\Documents\\Desktop\\Learn Data Science\\Linear Algebra")
f = open('stories_small.txt')
stories = list(f)
len(stories)
'''
word_list = {}
for i in range(len(stories)):
	if i == 0:
		word_list = set(stories[i].split())
	else:
		word_list = word_list|set(stories[i].split())
		
len(word_list)
'''

def makeInverseIndex(strlist):
	word_appear = {}
	for (i,doc) in enumerate(strlist):
		for word in doc.split():
			if word in word_appear:
				word_appear[word].add(i)
			else :
				word_appear[word] = set()
				word_appear[word].add(i)
	return(word_appear)
	
stories_word_list = makeInverseIndex(stories)


def orSearch(inverseIndex, query):
	ordoc = set()
	for word in query:
		if word in inverseIndex:
			ordoc.update(inverseIndex[word])
	return ordoc

orSearch(stories_word_list,['story','love'])

def andSearch(inverseIndex, query):
	anddoc = set(range(len(stories)))
	for word in query:
		if word in inverseIndex:
			anddoc = anddoc & inverseIndex[word]
	return anddoc

andSearch(stories_word_list,['story','love'])

# Problems
# Problem 0.8.1
def increments(L) : return [x+1 for x in L]

# Problem 0.8.2
def cubes(L) : return [z**3 for z in L]

#Problem 0.8.3
def tuple_sum(A,B) : return [(a+x,b+y) for ((a,b),(x,y)) in list(zip(A,B))]

#Problem 0.8.4
def inv_dict(d) : return {v:k for (k,v) in d.items()} 

# Problem 0.8.5
def row(p,n) : return [p+i for i in range(n)]

[row(i,20) for i in range(2,17)]
[[x+i for i in range(20)]  for x in range(2,17)]
