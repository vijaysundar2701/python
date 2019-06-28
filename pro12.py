aa,bb=map(int,input().split())
cc=[]
dd=[]
ee=[int(aa) for aa in input().split()]
for i in range(0,bb):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        dd.append(ee[j])
    vj=sum(dd)
    cc.append(vj)
print(cc[0])
for x in range(1,len(cc)):
    print(cc[x]- cc[x- 1])
