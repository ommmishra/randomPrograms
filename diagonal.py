lis =[[3,4,5],[8,78,9],[67,9,0]]
print(lis)

z = len(lis)

for i in range(0,z):
    x = 0
    y = i
    while(x <= i):
        if(i == 0):
            print(lis[i][x])
        else:
            print(lis[y-x][x])
        x = x + 1
    print(" ")
y = z - 1
l = 1
for i in range(z,0,-1):
    u = i-1
    x = 0
    while(u > 0):
        print(lis[y-x][l+x])
        u = u - 1
        x = x + 1
    l = l + 1
    print(" ")
