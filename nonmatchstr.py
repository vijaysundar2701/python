az,bx=input().split()
vk=abs(len(az)-len(bx))
for i in range(len(az)):
    if len(bx)==1 and bx[i] in az:
        break
    if az[i]!=bx[i]:
        vk+=1
print(vk)
