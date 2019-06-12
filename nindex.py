n=int(input())
k=list(map(int,input().split()))[:n]
for i in range(0,n):
    print(k[i],k.index(k[i]))
