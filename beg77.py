vr=int(input())
b=[]
for i in range(1,vr+1):
    if vr%i==0:
        b.append(i)
print(*b,sep=" ")
