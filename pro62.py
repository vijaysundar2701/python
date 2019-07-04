vj=input()
sub=""
f=0
p=[]
if vj==vj[::-1]:
  p.append(0)
for i in range(0,len(vj)-1):
  for j in range(i+1,len(vj)):
    sub=vj[i:j+1]
    if sub==sub[::-1]:
      p.append(len(vj)-len(sub))
print(min(p))
