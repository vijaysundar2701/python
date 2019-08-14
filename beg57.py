p,q=map(int,input().split())
k=list(map(int,input().split()))[:p]
if q in k:
    c=k.count(q)
    print(c)
