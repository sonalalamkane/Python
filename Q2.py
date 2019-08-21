X,Y=raw_input("Enter value of X and Y=").split(",")

result=[]

for i in range(int(X)):
	r=[]
	for j in range(int(Y)):
		mul=i*j
		r.append(mul)
	result.append(r)

print(result)
