hi=int(input())
w=list(map(int,input().split()))
m=0
for c in range(len(w)-2):
   for d in range(c+1,len(w)-1):
         for e in range(d+1,len(w)):
            if w[c]<w[d]<w[e] and c<d<e:
                m+=1
print(m)    
