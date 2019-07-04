vj=input()
vk=input()
i=vj.index("|")
mn=vj[:i]
k=vj[i+1:]
ax=mn+vk
by=k+vk
if len(mn)==len(by):
    l=mn+"|"+k+vk
    print(l)
elif len(k)==len(ax):
    l=mn+vk+"|"+k
    print(l)
else:
    print("Impossible")
