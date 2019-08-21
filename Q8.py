class generator(object):
	def __init__(self,number):
		self.number=number

	def generator_function(self):
		for x in range(self.number):
			if(x%7==0):
				yield x
			else:
				pass

search_range=int(raw_input("Enter value on N="))
obj=generator(search_range)
result=obj.generator_function()

for x in result:
	print(x)
