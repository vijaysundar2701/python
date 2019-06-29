ab=int(input())
cd=list(map(int,input().split()))
xy=[1]*ab
for i in range(ab):
    if i==0:
        if cd[i]>cd[i+1]:
            xy[i]=xy[i]+xy[i+1]
    elif i>0:
        if cd[i]>cd[i-1]:
            xy[i]=xy[i]+xy[i-1]
print(sum(xy))
