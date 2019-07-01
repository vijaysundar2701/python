vj,vk=map(int,input().split())
sv=list(map(int,input().split()))
vs=list(map(int,input().split()))
tt=[]
cin=0
for i in range(vj):
    y=vs[i]/sv[i]
    tt.append(y)
while vk>=0 and len(tt)>0:
    mindex=tt.index(max(tt))
    if vk>=sv[mindex]:
        cin=cin+sv[mindex]
        vk=vk-sv[mindex]
    sv.pop(mindex)
    vs.pop(mindex)
    tt.pop(mindex)
print(cin)
