ts=int(input())
ls=list(map(int,input().split()))
ss=[]
a=1
for i in range(ts-1):
    if ls[i]<ls[i+1]:
        a+=1
    else:
        ss.append(a)
        a=1
ss.append(a)
print(max(ss))
