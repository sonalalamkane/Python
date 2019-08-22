# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

class NotaStringException(Exception):
	def __init__(self,str):
		self.str=str

	def __str__(self):
		return(self.str)

try:
	string=raw_input("Enter strings which you want to sort in the form of comma separated value=")
	str_input  = string.split(",")

	"""
		It prints the given strings in the sorted order.
	"""
	for x in str_input:
		if(re.search("^[^a-zA-Z]+$",x)):
			raise NotaStringException()
		result=sorted(str_input)
	print(','.join(result))
except:
	print("The given input is not in string form.")