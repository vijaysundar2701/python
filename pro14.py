vj,vk=map(int,input().split())
lis=list(map(int,input().split()))
vj=[]
lis.insert(0,0)
for y in range(vk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=lis[i]     
     vj.append(sumup)
for y in vj:
    print(y)
