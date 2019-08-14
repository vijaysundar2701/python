w=list(input())
c=0
for i in w:
    if i=="0" or i=="1":
        c=c+1
if c==len(w):
    print("yes")
else:
    print("no")

