x = "Python is fun, Python?"
y = "Python"
z=0
a=0
z=len(y)

while(len(x)>z-1):
	result=x.find(y, a, z)
	# print(a)
	# print(z)
	if(result!=-1):
		print(result)
		print(z-1)
		a = z
		z = z+1
		print(" ")

	elif(result==-1):
		z = z+1
