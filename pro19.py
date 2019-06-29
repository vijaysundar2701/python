vj=int(input())
vk=list()
for i in range(vj):
    bm=input().split()
    bm=[int(d) for d in bm]
    for j in bm:
        vk.append(j)
vk.sort()
for i in vk:
    print(i,end=" ")
