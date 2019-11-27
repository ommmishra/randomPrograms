N,Q = input().split()
N = int(N)
Q = int(Q)
bin = list(map(int, input().split()))
for i in range(Q):
    query = list(map(int, input().split()))
    if(query[0]==0):
        if(bin[query[2]-1] == 0):
            print("EVEN")
        else:
            print("ODD")
    if(query[0]==1):
        query[1] = query[1] - 1
        if(bin[query[1]]==0):
            bin[query[1]] = 1
        else:
            bin[query[1]] = 0