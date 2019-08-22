# Question 4:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

class NotaBinaryException(Exception):
	def __init__(self,bin):
		self.bin=bin

	def __str__(self):
		return(self.bin)

try:
	binary_string=raw_input("Enter binary values in the form of comma separated value=")
	bin_input  = binary_string.split(",")
	result=[]

	"""
		In this the output is the binary value which is completely divided by 5.
	"""

	for x in bin_input:
		if(re.search("^[^0|1]+$",x)):
			raise NotaBinaryException()
		remainder=int(x,2)
		if((remainder%5)==0):
			result.append(x)

	print(",".join(result))
except:
	print("The given input is not in binary form.")
