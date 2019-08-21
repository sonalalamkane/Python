import re

password=raw_input("Enter passwords separated by comma=")
password_str = password.split(",")

for x in password_str:
	res=re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$*])(?=.{8,})",x)
	if(res):
		print(x)

