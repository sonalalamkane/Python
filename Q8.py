# Question 8:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

import re

class NotaNumberException(Exception):
	def __init__(self,num):
		self.num=num

	def __str__(self):
		return(self.num)

class generator:
	"""
		This will give result i.e values which are divisible by 7. 
	"""
	def __init__(self,number):
		"""
			The constructor for generator class.

			Parameters:
				number(int): The range in which the divide by 7 result you want to find i.e from 0 to number.
		"""
		self.number=number

	def generator_function(self):
		"""
			The function to give result i.e values which is divisible by 7.
		"""
		for x in range(self.number):
			if(x%7==0):
				yield x
			else:
				pass

try:
	search_range=raw_input("Enter value on N=")
	if(re.search("\D",search_range)):
		raise NotaNumberException()
	search_range=int(search_range)
	obj=generator(search_range)
	result=obj.generator_function()

	for x in result:
		print(x)
except:
	print("The given input is not a number.please enter valid input")
