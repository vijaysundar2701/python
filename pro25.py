q=int(input())
l=list(map(int,input().split()))
ss=[]
v=1
for i in range(q-1):
    if l[i]<l[i+1]:
        v+=1
    else:
        ss.append(v)
        v=1
ss.append(v)
print(max(ss))
