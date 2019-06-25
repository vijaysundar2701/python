q=int(input())
hi=list(map(int,input().split()))
oi=max(hi)
x,y=0,0
for i in range(0,len(hi)-1):
  for j in range(i+1,len(hi)):
    if abs(hi[i]+hi[j])<oi:
      x,y=hi[i],hi[j]
      oi=abs(x+y)
print(x,y)
