# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]X=
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input. 

import math
import re

class NotaNumberException(Exception):
	def __init__(self,num):
		self.num=num

	def __str__(self):
		return(self.num)

C=50
H=30

try:
	D=raw_input("Enter value of D separated by comma=")
	input_D  = D.split(",")

	"""
		This will print the result calculated by using the given formula.
	"""
	for x in input_D:
		if(re.search("\D",x)):
			raise NotaNumberException(x)
		Q=math.sqrt((2 * int(C) * int(x))/int(H))
		print(int(Q))
except:
	print("The given input is not a number.please enter valid input")