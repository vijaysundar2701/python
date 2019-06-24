f=int(input())
g=list(map(int,input().split()))
h=sorted(g)[::-1]
l=""
if(g==h):
   print(g[0])
else:
    for k in h:
        l=l+str(k)
    print(int(l))
