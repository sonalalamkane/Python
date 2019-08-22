# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

sentence=raw_input("Enter sentence=")

letter_count=0
digit_count=0

"""
	This will calculate the how many letters and how many digits in the given sentence.
"""

for x in sentence:
	if(x.isdigit()):
		digit_count=digit_count+1
	else:
		letter_count=letter_count+1

print"Number of letters in sentence=%d"%letter_count
print"Number of digits i sentence=%d"%digit_count