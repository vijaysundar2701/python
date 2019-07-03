hi,oi=map(int,input().split())
vj=list(map(int,input().split()))
vj=sorted(vj)
vk,i=0,0
flag=0
while i<len(vj)-2:
  a,b,c=vj[i:i+3]
  for j in range(0,oi):
    a,b,c=a+1,b+1,c+1 
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
      flag=0
  if flag==1:
    vk+=1
  i+=3
  a,b,c=0,0,0
print(vk)
