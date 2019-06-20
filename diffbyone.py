x,y= map(str,input().split())
c= 0
for i in range(len(x)):
  if x[i]!=y[i]:
    c=c+1
if c==1:
  print ("yes")
else:
  print ("no")
