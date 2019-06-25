x=int(input())
y=list(map(int,input().split()))
h=[]
l=[]
for i in range(0,len(y)):
    if i==y[i]:
        h.append(i)
    elif y[i]%2==0 and i!=y[i]:
        l.append(y[i])
    else:
        l.append(y[i])
print(*l,sep=' ')        
        
