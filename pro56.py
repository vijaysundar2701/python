vj,vk=map(int,input().split())
sec=list(map(int,input().split()))
con=0
for i in sec:
  a=86400-i
  vk=vk-a
  con+=1
  if vk<=0:
    break  
print(con)
