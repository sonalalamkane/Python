sentence=raw_input("Enter sentence=")

letter_count=0
digit_count=0

for x in sentence:
	if(x.isdigit()):
		digit_count=digit_count+1
	else:
		letter_count=letter_count+1

print"Number of letters in sentence=%d"%letter_count
print"Number of digits i sentence=%d"%digit_count