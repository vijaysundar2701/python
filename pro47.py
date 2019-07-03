az,vj=map(int,input().split())
if az%10==0:
  az=str(az)
  c=0
  for i in range(len(az)-1,-1,-1):
    if az[i]=='0':
      c+=1
  if vj<=c:
    print(az)
  else:
    az=az[:-c]
    az=az+'0'*vj
    print(az)
elif 10%(az%10)==0:
  vk=int('1'+'0'*vj)
  while True:
    if vk%az==0:
      print(vk)
      break
    else:
      vk+=int('1'+'0'*vj)
else:
  print(str(az)+vj*'0')
