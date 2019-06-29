sh=int(input())
se=list(map(int,input().split()))
x=[1]*sh
for i in range(sh):
    if i==0:
        if se[i]>se[i+1]:
            x[i]=x[i]+x[i+1]
    elif i>0:
        if se[i]>se[i-1]:
            x[i]=x[i]+x[i-1]
print(sum(x))
