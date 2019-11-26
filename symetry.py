T = int(input())
for i in range(T):
	N = int(input())
	a = []
	
	for j in range(N):
	    a.append(list(map(int, input().split())))
	    
	d = True
	
	n = N
	
	l = 0
	
	while l < n//2 and d:
	    for m in range(n//2):
	        if(a[l][m] != a[n-1-l][n-1-m] or a[l][m] != a[n-1-l][m] or a[l][m] != a[l][n-1-m]):
	            d = False
	    l = l + 1
	   
	if(n%2 != 0):
	    num = n//2
	    for k in range(n//2):
	        if(a[k][num] != a[n-1-k][num] or a[num][k] != a[num][n-1-k]):
	            d = False
	            break
	if(d):
		print("YES")
	else:
		print("NO")
