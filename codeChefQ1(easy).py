T = int(input())
f = []
val = None
for t in range(0,T):
	x = input()
	x = list(map(int, x.split(" ")))
	y = input()
	y = list(map(int, y.split(" ")))
	
	for i in range(0,x[1]):
		f.append(input())
	F = len(f)
	for i in range(0,F):
		f[i] = list(map(int, f[i].split(" ")))

	z = max(y)
	Z = x[2] - z
	
	if(Z != 0):
		f = []
		val = -1
		break
	else:
		val = x[2]
		print(val)



