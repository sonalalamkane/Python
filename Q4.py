binary_string=raw_input("Enter binary values in the form of comma separated value=")
bin_input  = binary_string.split(",")

result=[]

for x in bin_input:
	remainder=int(x,2)
	if((remainder%5)==0):
		result.append(x)

print(",".join(result))