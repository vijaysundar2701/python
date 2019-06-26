qq=int(input())
cc=[int(i) for i in input().split()]
yy=0
for i in range(qq):
   for j in range(i):
      if cc[j]<cc[i]:
         yy+=cc[j]
print(yy)         
