from itertools import combinations
x1,x2=input().split()
l=str(x1)
m=int(x2)
n=[]
o=combinations(l,len(l)-m)
for i in list(o):
    n.append("".join(i))
print(min(n))
