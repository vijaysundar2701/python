x=int(input())
y=list(map(int,input().split()))
l=[]
for i in range(0,len(y)):
    if y[i]%2==0 and i%2==1:
        l.append(y[i])
    elif y[i]%2==1 and i%2==0:
        l.append(y[i])
print(*l,sep=' ')   
