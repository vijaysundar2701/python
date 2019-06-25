c=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
  if(d.count(i)>1):
    e.append(i)    
  else:
    print(i)
