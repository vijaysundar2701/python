vj=int(input())
vk=list(map(int,input().split()))
az=0
by=0
vk.sort(reverse=True)
for i in vk:
  vk=az+i
  if by>vk:
    az=vk
  else:
    az=by
    by=vk
print(az,by)
