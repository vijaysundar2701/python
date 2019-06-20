n,m=map(int,input().split())
l=[]
for i in range(n,m+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
print(len(l))
            
