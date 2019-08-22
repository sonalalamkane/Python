# -*- coding: utf-8 -*-
# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

import re

class NotaNumberException(Exception):
	def __init__(self,num):
		self.num=num

	def __str__(self):
		return(self.num)

class NoOfArgException(Exception):
	pass

try:
	X,Y=raw_input("Enter value of X and Y=").split(",")
	result=[]

	"""
		This program prints the result i.e result of i*j which is given expression and i is nothing but row and j is the column.  
	"""
	if(re.search("\D",X)):
			raise NotaNumberException(X)
	for i in range(int(X)):
		if(re.search("\D",Y)):
				raise NotaNumberException(Y)
		r=[]
		for j in range(int(Y)):
			mul=i*j
			r.append(mul)
		result.append(r)
	print(result)
except:
	print("The given input is not a number.please enter valid input")
