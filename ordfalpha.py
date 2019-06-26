vj,vk=input().split()
vs=0
if len(vj)>len(vk):
  vj,vk=vk,vj
p=0
while p<len(vj):
  vs+=(ord(vk[p])-ord(vj[p]))
  p+=1
for p in range(p,len(vk)):
  vs+=ord(vk[p])-ord('a')+1
print(vs)
