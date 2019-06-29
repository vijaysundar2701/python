az,by=map(int,input().split())
hh=list(map(int,input().split()))
hh.sort()
hh.reverse()
az=by
z=0
for i in hh:
    if(az>=i):
        nm=int(az/i)
        z=z+nm
        az=az-nm*i
    if az==0:
        break
if(az==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
