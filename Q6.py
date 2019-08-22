# Question 6:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

sentence=raw_input("Enter sentence=")

upper_count=0
lower_count=0

"""
	It will print the count of the How many upper case letters are present in the given string and how many lower case letters present in the given sentence. 
"""

for x in sentence:
	if(x.isupper()):
		upper_count=upper_count+1
	else:
		lower_count=lower_count+1

print"Number of Upper letters in sentence=%d"%upper_count
print"Number of lower letters i sentence=%d"%lower_count