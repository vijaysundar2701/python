p=int(input())
q=list(map(int,input().split()))
r=[]
for i in range(0,len(q)):
    if i==q[i]:
        r.append(q[i])
if len(r)>0:
    print(*r)
else:
    print("-1")
