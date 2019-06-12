r=int(input())
l=[]
for i in range(0,r):  
    u=input()
    l.append(u)
list=[]
for i in zip(*l):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
