vj,vs=map(int,input().split())
vk=[]
ss=[]
a=[int(vj) for vj in input().split() ]
for i in range(0,vs):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        ss.append(a[j])
    x=sorted(ss)
    vk.append(min(ss))
    del ss[:]
for sz in range(0,len(vk)):
    print(vk[sz])
