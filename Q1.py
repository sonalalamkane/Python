#Question No:1
import math

C=50
H=30
D=raw_input("Enter value of D separated by comma=")
input_D  = D.split(",")
print(input_D)

for x in input_D:
	Q=math.sqrt((2 * int(C) * int(x))/int(H))
	print(int(Q))