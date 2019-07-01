vj=int(input())
sk=0
rs=0
m=[]
while sk<90 and sk<vj:
  s=0
  for j in str(vj-sk):
    s+=int(j)
  if s+(vj-sk)==vj:
    rs+=1
    m.append(vj-sk)
  sk+=1
print(rs)
for sk in m:
  print(sk)
