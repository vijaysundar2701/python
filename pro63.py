vk=input()
mn=[]
for i in vk:
    if i not in mn:
        mn.append(i)
        #print(i)
    else:
        break
print(len(mn))
