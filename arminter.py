y,z=map(int,input().split())
lis=[]
for i in range(y,z):
    temp=i
    r=0
    while(i>=1):
        a=int(i%10)
        r=int(r+a*a*a)
        i=int(i/10)
        if temp==r and i==0:
            lis.append(r)
print(*lis,sep='  ')
    
