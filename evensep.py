low,high=map(int,input().split())
s=[]
for i in range(low+1,high):
    if i%2==0:
        s.append(i)
print(*s,sep='  ')
