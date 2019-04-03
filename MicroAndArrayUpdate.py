T = int(input())

for i in range(T):
    s,k = input().split(' ')
    k = int(k)
    x = input()
    print(x)
    x = list(map(int,x.split(' ')))
    x.sort()
    if(((k-x[0]) == 0) or ((k-x[0]) < 0)):
        print(0)
    else:
        print(k-x[0])