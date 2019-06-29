o=int(input())
w=[]
ki=bin(2**o-1)[2::]
lm=len(ki)
for i in range(0,2**o):
    f=bin(i)[2::]
    if len(f)<lm:
        w.append([f.count("1"),(lm-len(f))*"0"+f])
    else:
        w.append([f.count("1"),f])
w.sort()
for i in range(0,len(w)):
    print(w[i][1])
