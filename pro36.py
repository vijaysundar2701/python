v = int(input())
ss = [ int(x) for x in input().split()]
v = len(ss)
cc = 0
for i in range(0,v-2) :
    for j in range(i+1, v-1):
        for k in range(j+1, v):
            if cc[i] > cc[j] > cc[k] :
                cc += 1
print(cc)
