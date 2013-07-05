# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):  return [i for i in L if i%num!=0]



## Problem 2
def myLists(L): return [list(range(1,i+1)) for i in  L]



## Problem 3
def myFunctionComposition(f, g):  return {fkey:g[f[fkey]] for gkey in g for fkey in f}



## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c =  -1+0.001j
complex_addition_d = 0.001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): 
	s=0
	for i in L:
		s+=i
	return s



## Problem 7
def myProduct(L): 
	s=1
	for i in L:
		s=s*i
	return s




## Problem 8
def myMin(L): 
	s=L[0]
	for i in L[1:]:
		if i<s:
			s=i
	return s




## Problem 9
def myConcat(L): 
	s=''
	for i in L:
		s+=i
	return s



## Problem 10
def myUnion(L): 
	s=set({})
	for i in L:
		for key in i:
			if key  not in s:
				s.add(key)
	return s

