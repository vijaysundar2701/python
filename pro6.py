import math
vj=int(input())
vk=math.log10(vj)/math.log10(2)
if math.ceil(vk)==math.floor(vk):
    print(0)
else:
    hi=(vj-1)//2
    oi=hi*2
    print(vj-oi)
