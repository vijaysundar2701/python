def check(a):
        vk=1
        for v in range(0,len(a)-1):
                if a[v]!=a[v+1]:
                        vk=vk+1
                else:
                    break
        return vk
number=int(input())
vj=list(map(int,input().split()))
for v in range(0,len(vj)):
        if vj[v]>0:
                vj[v]=1
        else:
             vj[v]=0
q=""
for v in range(0,len(vj)):
        m=vj[v::]
        q=q+str(check(m))+" "
print(q.strip())
