vj=input()
f=0
for i in range(0,len(vj)-1):
  for j in range(i+1,len(vj)):
    if vj[i]<vj[j]:
      f=1
      print(vj[j:])
      break
  if f==1:
    break
else:
  print(vj)
