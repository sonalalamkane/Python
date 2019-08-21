string=raw_input("Enter strings which you want to sort in the form of comma separated value=")
str_input  = string.split(",")

result=sorted(str_input)

print(','.join(result))