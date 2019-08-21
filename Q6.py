sentence=raw_input("Enter sentence=")

upper_count=0
lower_count=0

for x in sentence:
	if(x.isupper()):
		upper_count=upper_count+1
	else:
		lower_count=lower_count+1

print"Number of Upper letters in sentence=%d"%upper_count
print"Number of lower letters i sentence=%d"%lower_count