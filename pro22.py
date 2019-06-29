vj=int(input())
vk=list(map(int,input().split()))
la=vk[1:vj:2]
lb=vk[0:vj:2]
if(sum(la)>=sum(lb)):
    print(sum(la))
else:
    print(sum(lb))
