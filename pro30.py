hh=input()
ab=0
for i in range(0,len(hh)):
    sv=hh[0:i]+hh[i+1::]
    if int(sv)%8==0:
        ab=1
        break
if ab==1:
    print("yes")
else:
    print("no")
