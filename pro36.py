u=int(input())
k=[int(i) for i in input().split()]
o=0
for i in range(1,u-1):
    if k[i]<k[i-1] and k[i]<k[i+1]:
        o+=1
    elif k[i]>k[i-1] and k[i]>k[i+1]:
        o+=1
print(o)
